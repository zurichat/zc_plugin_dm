from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
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
                    if centrifugo_data.get("status_code") < 400:
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

