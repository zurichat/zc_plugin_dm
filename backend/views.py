import json
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from rest_framework.serializers import Serializer
from .db import DB,send_centrifugo_data, get_user_rooms, get_rooms
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
        "plugin_id" : "6135f65de2358b02686503a7",
        "organisation_id" : f"{org_id}",
        "user_id" : f"{user}",
        "group_name" : "DM",
        "show_group" : False,
        "joined_rooms":[],
        "public_rooms": [
        {
            "id": "6139b26959842c7444fb01f5",
            "title": "Announcement",
            "members": 1250,
            "unread": 2,
            "action": "open"
        },
        {
            "id": "6139b29259842c7444fb01f6",
            "title": "Dorime",
            "members": 12,
            "unread": 0,
            "action": "open"
        },
        {
            "id": "6139b35259842c7444fb01f7",
            "title": "Ameno",
            "members": 20,
            "unread": 10,
            "action": "open"
        },
        {
            "id": "6139b74e59842c7444fb01fa",
            "title": "games",
            "members": 1250,
            "unread": 16,
            "action": "open"
        },
        {
            "id": "6139b88359842c7444fb01fc",
            "title": "business-ideas",
            "members": 500,
            "unread": 25,
            "action": "open"
        }
        ],
        # List of rooms/collections created whenever a user starts a DM chat with another user
        # This is what will be displayed by Zuri Main on the sidebar
        "DMs":rooms,
    }
    return JsonResponse(side_bar, safe=False)





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


def get_all_rooms():
    response = DB.read("dm_rooms")
    return response

@api_view(["GET"])
def getUserRooms(request):
    if request.method == "GET":
        res = get_rooms(request.GET.get("user_id", None))
        if request.GET.get("user_id") == None:
            return Response(get_all_rooms())
        else:
            if len(res) == 0:
                return Response(data="no such user", status=status.HTTP_204_NO_CONTENT)
            return Response(res)
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
    
@api_view(["POST", "GET"])
def reminder(request):
    """
        This is used to remind a user about a bookmarked message
        and scheduled message
    """
    #collect the user info(the rooms the user is in) , the message info (time of creation),
    # collect the scheduled message(time created, time set for the remineder)
    # set a default timer to count  of 24hours for bookmarked messages,
    #
    #return {message with 15 words, snooze ,dismiss }
    # so what can I implement
    #create a room for the current user to display reminders
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data['user_id']
        room_id = data['room_id']
        recipient = data['recipient_id']
        time = data['time']
        

    # serializers = ReminderSerializer
    # room_collection = "dm_rooms"
    # rooms = DB.read(room_collection)
    # get_user_rooms(collection_name, org_id, user)

