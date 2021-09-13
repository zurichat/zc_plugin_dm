import json
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status
import requests
from rest_framework.serializers import Serializer
from .db import *
# Import Read Write function to Zuri Core
from .serializers import MessageSerializer
from .serializers import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



def index(request):
    context = {}
    return render(request, 'index.html', context)


# Shows basic information about the DM plugin
def info(request):
    info = {
        "message": "Plugin Information Retrieved",
        "data": {
            "type": "Plugin Information",
            "plugin_info": {"name": "DM Plugin",
                            "description": ["Zuri.chat plugin", "DM plugin for Zuri Chat that enables users to send messages to each other"]
                            },
            "scaffold_structure": "Monolith",
            "team": "HNG 8.0/Team Orpheus",
            "sidebar_url": "https://dm.zuri.chat/api/v1/sidebar",
            "homepage_url": "https://dm.zuri.chat/"
        },
        "success": "true"
    }

    return JsonResponse(info, safe=False)


def verify_user_auth(token):
	"""
	Call Endpoint for verification of JWT Token
	Returns: py dict -> is_authenticated: boolean, & data: more info
	"""
	url = "https://api.zuri.chat/auth/verify-token"
	
	headers = {
		'Authorization': f'Bearer {token}',
		'Content-Type': 'application/json'
	}

	api_response = requests.request("GET", url, headers=headers)
	
	json_response = api_response.json()
	
	response = {}
	if json_response['status'] == "200":
		response['is_authenticated'] = json_response['data']['is_verified']
		response['data'] = json_response['data']['user']
	else:
		response['is_authenticated'] = False
		response['data'] = json_response['message']
	
	return response

# Returns the json data of the sidebar that will be consumed by the api
# The sidebar info will be unique for each logged in user
# user_id will be gotten from the logged in user
# All data in the message_rooms will be automatically generated from zuri core

    

def side_bar(request):
    collections = "dm_rooms"
    org_id = request.GET.get("org", None)
    user = request.GET.get("user", None)
    rooms = get_user_rooms(collections, org_id, user)

    side_bar = {
        "name" : "DM Plugin",
        "description" : "Sends messages between users",
        "plugin_id" : "6135f65de2358b02686503a7",
        "organisation_id" : f"{org_id}",
        "user_id" : f"{user}",
        "group_name" : "DM",
        "show_group" : False,
        "public_rooms":[],
        "joined_rooms":rooms,
        # List of rooms/collections created whenever a user starts a DM chat with another user
        # This is what will be displayed by Zuri Main 
    }
    return JsonResponse(side_bar, safe=False)



@swagger_auto_schema(methods=['post'], request_body=MessageSerializer, responses={400: 'Error Response'})
@api_view(["POST"])
def send_message(request):
    """
    This is used to send message to user in rooms.
    It checks if room already exist before sending data.
    It makes a publish event to centrifugo after data 
    is persisted
    """
    serializer = MessageSerializer(data=request.data)
    
    if serializer.is_valid():
        data = serializer.data
        room_id = data['room_id'] #room id gotten from client request
        
        rooms = DB.read("dm_rooms")
        if type(rooms) == list:
            is_room_avalaible = len([room for room in rooms if room.get('_id', None) == room_id]) != 0
        
            if is_room_avalaible:
                response = DB.write("dm_messages", data=serializer.data)
                if response.get("status") == 200:
                    centrifugo_data = send_centrifugo_data(room=room_id,data=data) #publish data to centrifugo
                    if centrifugo_data["message"].get("error",None) == None:
                        response_output = {
                            "status":response["message"],
                            "message_id":response["data"]["object_id"],
                            "data":{
                                "room_id":room_id,
                                "sender_id":data["sender_id"],
                                "message":data["message"]
                            }
                        }
                        return Response(data=response_output, status=status.HTTP_201_CREATED)
                    
                return Response(data="data not sent",status=status.HTTP_400_BAD_REQUEST)
            return Response("No such room",status=status.HTTP_400_BAD_REQUEST)    
        return Response("core server not avaliable",status=status.HTTP_424_FAILED_DEPENDENCY)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(methods=['post'], request_body=RoomSerializer, responses={400: 'Error Response'})
@api_view(["POST"])
def create_room(requests):
    serializer = RoomSerializer(data=requests.data)

    if serializer.is_valid():
        response = DB.write("dm_rooms", data=serializer.data)
        data = dict(room_id=response.get("data").get("object_id"))
        if response.get("status") == 200:
            return Response(data=data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getUserRooms(request):
    """
    This is used to retrieve all rooms a user is currently active in.
    It takes in a user_id as query param and returns the rooms for that user or a 204 status code 
    if there is no room for the user_id or an invalid user_id.
    If the user_id is not provided, a 202 status code is returned.
    """
    if request.method == "GET":
        res = get_rooms(request.GET.get("user_id", None))
        param = len(request.GET.dict())
        if param == 1:
            if request.GET.get("user_id") == None:
                return Response(data="Provide a user_id as query param", status=status.HTTP_202_ACCEPTED)
            else:
                if len(res) == 0:
                    return Response(data="No rooms available", status=status.HTTP_204_NO_CONTENT)
                return Response(res, status=status.HTTP_200_OK)
        elif param == 0:
            return Response(data="Provide a user_id as query param", status=status.HTTP_202_ACCEPTED)
        return Response(data="Provide only the user_id", status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def getRoomMessages(request):
    """
    This is used to retrieve messages in a room. It takes a room_id or a date as query params.
    If only the room_id is provided, it returns a list of all the messages if available,
    or a 204 status code if there is no message in the room or invalid room_id.
    If only the date param is provided, it returns a 202 status code. 
    If both room_id and date are provided, it returns all the messages in that room for that
    particular date.
    If there is no query parameter, it returns a 202 status code.
    """
    if request.method == "GET":
        room = request.GET.get("room_id", None)
        date = request.GET.get("date", None)
        params = request.GET.dict()
        print(params)
        allow = False
        if len(params) == 0 or len(params) > 2:
            allow = False
        elif len(params) == 1 and "room_id" in params:
            allow = True
        elif len(params) == 2 and "room_id" in params and "date" in params:
            allow = True
        else:
            allow = False
        res = get_room_messages(room)
        if allow:
            if room != None and date != None:
                response_data = get_messages(res, date)
                if len(response_data) == 0:
                    return Response(data="No messages available", status=status.HTTP_204_NO_CONTENT)
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                if len(res) == 0:
                    return Response(data="No messages available", status=status.HTTP_204_NO_CONTENT)
                return Response(res, status=status.HTTP_200_OK)
        return Response(data="Provide the room_id or/and date only as params", status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def room_info(request):
    """
    This is used to retrieve information about a room.
    """
    room_id = request.GET.get("room_id", None)
    # org_id = request.GET.get("org_id", None)
    room_collection = "dm_rooms"
    rooms = DB.read(room_collection)
    if rooms is not None:
        for current_room in rooms:
            if current_room['_id'] == room_id:
                if 'room_user_ids' in current_room:
                    room_user_ids = current_room['room_user_ids']
                else:
                    room_user_ids =""
                if 'created_at' in current_room:
                    created_at = current_room['created_at']
                else:
                    created_at =""
                if 'org_id' in current_room:
                    org_id = current_room['org_id']
                else:
                    org_id ="6133c5a68006324323416896"
                room_data = {
                    "room_id": room_id,
                    "org_id": org_id,
                    "room_user_ids": room_user_ids,
                    "created_at": created_at,
                    "description": f"This room contains the coversation between {room_user_ids[0]} and {room_user_ids[1]}"
                }
                return Response(data=room_data, status=status.HTTP_200_OK)
        return Response(data="No such Room", status=status.HTTP_400_BAD_REQUEST)
    return Response(data="No Rooms", status=status.HTTP_400_BAD_REQUEST)
    