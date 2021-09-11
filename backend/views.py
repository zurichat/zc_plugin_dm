import json
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
import requests
from rest_framework.serializers import Serializer
from .db import DB,send_centrifugo_data, get_user_rooms 
# Import Read Write function to Zuri Core
from .serializers import MessageSerializer
from .serializers import *



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
        "plugin_id" : "dm-plugin-id",
        "organisation_id" : "HNGi8",
        "user_id" : "232",
        "group_name" : "DM",
        "show_group" : False,
        "Public rooms":[],
        "Joined rooms":[],
        # List of rooms/collections created whenever a user starts a DM chat with another user
        # This is what will be displayed by Zuri Main on the sidebar
        "DMs":rooms,
    }
    return JsonResponse(side_bar, safe=False)





@api_view(["POST"])
def send_message(request):
    """
    this is used to send message to user in rooms
    It checks if room already exist before sending data
    Ir makes a publish event to centrifugo after data 
    is persiste
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
                    print("data sent to zc core")
                    centrifugo_data = send_centrifugo_data(room=room_id,data=data) #publish data to centrifugo
                    if centrifugo_data["message"].get("error",None) == None:
                        print(centrifugo_data)
                        return Response(data=response, status=status.HTTP_201_CREATED)
                    
                return Response(data="data not sent",status=status.HTTP_400_BAD_REQUEST)
            return Response("No such room",status=status.HTTP_400_BAD_REQUEST)    
        return Response("core server not avaliable",status=status.HTTP_424_FAILED_DEPENDENCY)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def create_room(requests):
    serializer = RoomSerializer(data=requests.data)

    if serializer.is_valid():
         response = DB.write("dm_rooms", data=serializer.data)
         data = dict(room_id=response.get("data").get("object_id"))
         if response.get("status") == 200:
            return Response(data=data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def edit_room(request, pk):
    try: 
        data = DB.read("dm_rooms",{"id":pk})
    except: 
        return JsonResponse({'message': 'The room does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET':
        singleRoom = DB.read("dm_rooms",{"id": pk})
        return JsonResponse(singleRoom) 
 
    elif request.method == 'PUT': 
        room_serializer = RoomSerializer(data, data=request.data) 
        if room_serializer.is_valid(): 
            response = DB.write("dm_rooms", data=room_serializer.data)
            return Response(room_serializer.data)
        return Response(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        

@api_view(["POST"])
def room_info(request):
    serializer = RoomInfoSerializer(data=request.data)
    room_collection = "dm_rooms"
    rooms = DB.read(room_collection)
    message_collection = "dm_messages"
    messages  = DB.read(message_collection)
    room_messages=[]
    
    if serializer.is_valid():
        data = serializer.data
        room_id = data['room_id']
        for message in messages:
            if 'room_id' in message and message['room_id'] == room_id:
                room_messages.append(message)
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
                    org_id =""

                room_data = {
                    "room_id": room_id,
                    "org_id": org_id,
                    "room_user_ids": room_user_ids,
                    "created_at": created_at,
                    "messages": room_messages
                }
                return Response(data=room_data, status=status.HTTP_200_OK)
        return Response(data="No such Room", status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)
