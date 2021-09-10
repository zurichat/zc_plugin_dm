from django.http.response import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

import requests

# Import Read Write function to Zuri Core
from .db import DB

from .serializers import *
from backend import serializers


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
    side_bar = {
        "name" : "DM Plugin",
        "description" : "Sends messages between users",
        "plugin_id" : "dm-plugin-id",
        "organisation_id" : "HNGi8",
        "user_id" : "232",
        "group_name" : "DM",
        "show_group" : False,
        # List of rooms/collections created whenever a user starts a DM chat with another user
        # This is what will be displayed by Zuri Main on the sidebar
        "message_rooms":[
            {
                "room_id":"collection_id",
                "partner":"username of chat-partner",
                "room_url":"https://dm.zuri.chat/api/organizations/id/rooms/id",
                "status":"active",
                "latest_message":"unread",
            },
            {
                "room_id":"collection_id",
                "partner":"username of chat-partner",
                "room_url":"https://dm.zuri.chat/api/organizations/id/rooms/id",
                "status":"active",
                "latest_message":"unread",
            },
            {
                "room_id":"collection_id",
                "partner":"username of chat-partner",
                "room_url":"https://dm.zuri.chat/api/organizations/id/rooms/id",
                "status":"active",
                "latest_message":"unread",
            },
            {
                "room_id":"collection_id",
                "partner":"username of chat-partner",
                "room_url":"https://dm.zuri.chat/api/organizations/id/rooms/id",
                "status":"active",
                "latest_message":"unread",
            },
            {
                "room_id":"collection_id",
                "partner":"username of chat-partner",
                "room_url":"https://dm.zuri.chat/api/organizations/id/rooms/id",
                "status":"active",
                "latest_message":"read",
            },
            {
                "room_id":"collection_id",
                "partner":"username of chat-partner",
                "room_url":"https://dm.zuri.chat/api/organizations/id/rooms/id",
                "status":"deleted",
                "latest_message":"read",
            },
            {
                "room_id":"collection_id",
                "partner":"username of chat-partner",
                "room_url":"https://dm.zuri.chat/api/organizations/id/rooms/id",
                "status":"deleted",
                "latest_message":"read",
            },
            {
                "room_id":"collection_id",
                "partner":"username of chat-partner",
                "room_url":"https://dm.zuri.chat/api/organizations/id/rooms/id",
                "status":"deleted",
                "latest_message":"read",
            },
        ],
    }
    return JsonResponse(side_bar, safe=False)


@api_view(["POST"])
def save_message(request):
    serializer = MessageSerializer(data=request.data)
    
    if serializer.is_valid():
        response = DB.write("dm_messages", data=serializer.data)
        if response and response.get("status_code") == 201:
            return Response(
                data=response, status=status.HTTP_201_CREATED)
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

