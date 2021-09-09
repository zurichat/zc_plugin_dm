
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime
import requests

# Import Read Write function to Zuri Core
from .db import DB, get_user_rooms

from .serializers import MessageSerializer
from .serializers import RoomSerializer


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

 
def verify_user_auth(ID, token):
	url = f"https://api.zuri.chat/users/{ID}"
	headers = {
		'Authorization': f'Bearer {token}',
		'Content-Type': 'application/json'
	}
	response = requests.request("GET", url, headers=headers)
	
	return response.status == "200"


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
        # List of rooms/collections created whenever a user starts a DM chat with another user
        # This is what will be displayed by Zuri Main on the sidebar
        "DMs":rooms,
    }
    return JsonResponse(side_bar, safe=False)


@api_view(["POST"])
def create_room(request):
    collection_name="dm_rooms"
    org_id = request.data["org_id"]
    id1 = request.data["id1"]
    id2 = request.data["id2"]
    username1 = request.data["username1"]
    username2 = request.data["username2"]
    room = RoomSerializer(org_id=org_id, id1=id1, id2=id2, name1=username1,name2=username2)
    room.serialize()
    print(room)


@api_view(["POST"])
def save_message(request):
    serializer = MessageSerializer(data=request.data)
    
    if serializer.is_valid():
        response = DB.write("dm_messages", data=serializer.data)
        if response and response.get("status_code") == 201:
            return Response(
                data=response, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
