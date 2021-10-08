import json
from typing import Dict, List
import uuid
import re
from django.http import response
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import generic
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework import status, generics
import requests
import time
from .utils import send_centrifugo_data
from .db import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import (
    APIView,
    exception_handler,
)
from django.core.files.storage import default_storage
# Import Read Write function to Zuri Core
from .resmodels import *
from .serializers import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from datetime import datetime
import datetime as datetimemodule
from .centrifugo_handler import centrifugo_client
from rest_framework.pagination import PageNumberPagination
from .decorators import db_init_with_credentials
from queue import LifoQueue


@swagger_auto_schema(
    methods=["post"],
    request_body=RoomSerializer,
    operation_summary="Creates a new room between users",
    responses={
        200: "ok: Room already exist",
        201: CreateRoomResponse,
        400: "Error: Bad Request",
    },
)
@api_view(["POST"])
@db_init_with_credentials
def create_room(request, member_id):
    """
    Creates a room between users.
    It takes the id of the users involved, sends a write request to the database .
    Then returns the room id when a room is successfully created
    """
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        user_ids = serializer.data["room_member_ids"]
        
        if len(user_ids) > 2:
            # print("            --------MUKHTAR-------              \n\r")        
            response = group_room(request, member_id)
            if response.get('get_group_data'):
                return Response(data=response['room_id'], status=response['status_code'])
        
        else:
            # print("            --------FAE-------              \n\r")        
            user_ids = serializer.data["room_member_ids"]
            user_rooms = get_rooms(user_ids[0], DB.organization_id)
            if "status_code" in user_rooms:
                pass
            else:
                for room in user_rooms:
                    room_users = room["room_user_ids"]
                    if set(room_users) == set(user_ids):
                        response_output = {
                                                "room_id": room["_id"]
                                            }
                        return Response(data=response_output, status=status.HTTP_200_OK)
			
            fields = {"org_id": serializer.data["org_id"],
                      "room_user_ids": serializer.data["room_member_ids"],
                      "room_name": serializer.data["room_name"],
                      "private": serializer.data["private"],
                      "created_at": serializer.data["created_at"],
                      "bookmark": [],
                      "pinned": [],
                      "starred": [ ]
                          }

            response = DB.write("dm_rooms", data=fields)
            # ===============================

        data = response.get("data").get("object_id")
        if response.get("status") == 200:
            response_output = {
                    "event": "sidebar_update",
                    "plugin_id": "dm.zuri.chat",
                    "data": {
                        "group_name": "DM",
                        "name": "DM Plugin",
                        "show_group": False,
                        "button_url": "/dm",
                        "public_rooms": [],
                        "joined_rooms": sidebar_emitter(org_id=DB.organization_id, member_id=member_id, group_room_name=serializer.data["room_name"])  # added extra param
                    }
            }

            try:
                centrifugo_data = centrifugo_client.publish (
                    room=f"{DB.organization_id}_{member_id}_sidebar", data=response_output )  # publish data to centrifugo
                if centrifugo_data and centrifugo_data.get ( "status_code" ) == 200:
                    return Response ( data=response_output, status=status.HTTP_201_CREATED )
                else:
                    return Response(
                        data="room created but centrifugo failed",
                        status=status.HTTP_424_FAILED_DEPENDENCY,
                    )
            except:
                return Response(
                    data="centrifugo server not available",
                    status=status.HTTP_424_FAILED_DEPENDENCY,
                )
        return Response("data not sent", status=status.HTTP_424_FAILED_DEPENDENCY)
    return Response(data="Invalid data", status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["get"],
    operation_summary="Retrieves all rooms linked to a user id",
    query_serializer=UserRoomsSerializer,
    responses={
        200: "OK: Success",
        204: "No Rooms Available",
        400: "Error: Bad Request",
    },
)
@api_view(["GET"])
@db_init_with_credentials
def user_rooms(request, user_id):
    """
    Retrieves all rooms a user is currently active in.
    if there is no room for the user_id it returns a 204 status response.
    """
    if request.method == "GET":
        print(DB.organization_id)
        res = get_rooms(user_id, DB.organization_id)
        if res == None:
            return Response(
                data="No rooms available", status=status.HTTP_204_NO_CONTENT
            )
        return Response(res, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(
    methods=["get"],
    operation_summary="Retrieves all the information about a room",
    query_serializer=RoomInfoSerializer,
    responses={
        200: RoomInfoResponse,
        400: "Error: Bad Request",
        404: "Error: Room Not Found",
    }
)
@api_view(["GET"])
@db_init_with_credentials
def room_info(request, room_id):
    """
    Retrieves information about a room.
    It takes the room id and searches the dm_rooms collection
    If the room exists, a json response of the room details is returned
    Else a 404 response is returned with a "No such room" message
    """
    # room_id = request.GET.get("room_id", None)
    org_id = DB.organization_id
    room_collection = "dm_rooms"
    current_room = DB.read(room_collection, {"_id": room_id})

    if current_room and current_room.get("status_code", None) == None:

        if "room_user_ids" in current_room:
            room_user_ids = current_room["room_user_ids"]
        elif "room_member_ids" in current_room:
            room_user_ids = current_room["room_member_ids"] 
        else:
            room_user_ids = ""
        if "starred" in current_room:
            starred = current_room["starred"]
        else:
            starred = ""
        if "pinned" in current_room:
            pinned = current_room["pinned"]
        else:
            pinned = ""
        if "bookmark" in current_room:
            bookmark = current_room["bookmark"]
        else:
            bookmark = ""
        if "private" in current_room:
            private = current_room["private"]
        else:
            private = ""
        if "created_at" in current_room:
            created_at = current_room["created_at"]
        else:
            created_at = ""
        if "org_id" in current_room:
            org_id = current_room["org_id"]
        if "room_name" in current_room:
            room_name = current_room["room_name"]
        else:
            room_name = ""

        if len(room_user_ids) > 3:
            text = f" and {len(room_user_ids)-2} others"
        elif len(room_user_ids) == 3:
            text = " and 1 other"
        else:
            text = " only"
        if  len(room_user_ids) >= 1:
            user1 = get_user_profile(org_id=org_id, user_id=room_user_ids[0])
            if user1["status"] == 200:
                user_name_1 = user1["data"]["user_name"]
            else:
                user_name_1 = room_user_ids[0]
        else: 
            user_name_1 = "Some user"
        if len(room_user_ids) > 1:
            user2 = get_user_profile(org_id=org_id, user_id=room_user_ids[1])
            if user2["status"] == 200:
                user_name_2 = user2["data"]["user_name"]
            else:
                user_name_2 = room_user_ids[1]
        else:
            user_name_2 = "Some user"
        room_data = {
            "room_id": room_id,
            "org_id": org_id,
            "room_name": room_name,
            "room_user_ids": room_user_ids,
            "created_at": created_at,
            "description": f"This room contains the coversation between You and {user_name_2}{text}",
            "starred": starred,
            "pinned": pinned,
            "private": private,
            "bookmarks": bookmark,
            "Number of users": f"{len(room_user_ids)}",

        }
        return Response(data=room_data, status=status.HTTP_200_OK)
    return Response(data="Room not found", status=status.HTTP_404_NOT_FOUND)



@swagger_auto_schema(
    methods=["get"],
    operation_summary="searches for message by a user",
    responses={404: "Error: Not Found"},
)
@api_view(["GET"])
@db_init_with_credentials
def search_DM(request, member_id):

    keyword = request.query_params.get('keyword',"")
    users = request.query_params.getlist('id',[])
    limit = request.query_params.get('limit',20)

    try:
        if type(limit) == str: limit = int(limit)
    except ValueError:
        limit=20

    paginator = PageNumberPagination()
    paginator.page_size = limit

    try:
        rooms = DB.read("dm_rooms") #get all rooms
        user_rooms = list(filter(lambda room: member_id in room.get('room_user_ids',[]) or member_id in room.get('room_member_ids',[]), rooms)) #get all rooms with user        
        if users != []:
            rooms_checked = []
            for user in users:
                rooms_checked += [room for room in user_rooms
                            if set(room.get('room_user_ids',[])) == set([member_id,user]) or  set(room.get('room_member_ids',[])) == set([member_id,user])] #get rooms with other specified users
            user_rooms = rooms_checked
        all_messages = DB.read("dm_messages") #get all messages
        thread_messages = [] # get all thread messages
        for message in all_messages:
            threads  = message.get('threads',[])
            for thread in threads:
                thread['room_id'] = message.get('room_id')
                thread['message_id'] = message.get('_id')
                thread['thread'] = True
                thread_messages.append(thread)


        room_ids = [room['_id'] for room in user_rooms]

        user_rooms_messages = [message for message in all_messages
                                if message['room_id'] in room_ids and message['message'].find(keyword) != -1] #get message in rooms
        user_rooms_threads = [message for message in thread_messages
                                if message['room_id'] in room_ids and message['message'].find(keyword) != -1]

        user_rooms_messages.extend(user_rooms_threads)

        for message in user_rooms_messages:
            if 'read' in message.keys(): del message['read']
            if 'pinned' in message.keys():del message['pinned']
            if 'saved_by' in message.keys():del message['saved_by']
            if 'threads' in message.keys(): del message['threads']
            if 'thread' not in message.keys(): message['thread'] = False
        result_page = paginator.paginate_queryset(user_rooms_messages, request)
        return paginator.get_paginated_response(result_page)   
    except:
        return Response("Not Found", status=status.HTTP_404_NOT_FOUND)


def group_room(request, member_id):
	serializer = RoomSerializer(data=request.data)
	if serializer.is_valid():
		user_ids = serializer.data["room_member_ids"]
		
		if len(user_ids) > 9:
			response = {
				"get_group_data": True,
				"status_code": 400,
				"room_id": "Group cannot have over 9 total users"
			}
			return response
		else:
			all_rooms = DB.read("dm_rooms")
			group_rooms = []
			for room_obj in all_rooms:
				try:
					room_members = room_obj['room_user_ids']
					if len(room_members) > 2 and set(room_members) == set(user_ids):
						group_rooms.append(room_obj['_id'])
						response = {
							"get_group_data": True,
							"status_code": 200,
							"room_id": room_obj["_id"]
						}
						return response
				except KeyError:
					pass
					# print("Object has no key of Serializer")
			
			# print("group rooms =", group_rooms)
					
			fields = {
				"org_id": serializer.data["org_id"],
				"room_user_ids": serializer.data["room_member_ids"],
				"room_name": serializer.data["room_name"],
				"private": serializer.data["private"],
				"created_at": serializer.data["created_at"],
				"bookmark": [],
				"pinned": [],
				"starred": [ ]
			}
			response = DB.write("dm_rooms", data=fields)
			
		return response

@api_view(["PUT","GET"])
@db_init_with_credentials
def star_room(request, room_id, member_id):
    """
    Endpoint for starring and unstarring a user, it moves the user from the dm list to a starred dm list
    """
    if request.method == "PUT":
        room = DB.read("dm_rooms", {"_id": room_id})
        if room:
            if member_id in room.get("room_member_ids", []) or member_id in room.get("room_user_ids", []):
                data =  room.get("starred",[])
                if member_id in data:
                    data.remove(member_id)
                else:
                    data.append(member_id)

                response = DB.update("dm_rooms", room_id,{"starred":data})
                print(response)
                if response and response.get("status_code",None) == None:
                    return Response("Success", status=status.HTTP_200_OK)
                return Response(data="Room not updated", status=status.HTTP_424_FAILED_DEPENDENCY)
            return Response(data="User not in room", status=status.HTTP_404_NOT_FOUND)
        return Response("Invalid room", status=status.HTTP_400_BAD_REQUEST)

    
    elif request.method == "GET":
        room = DB.read("dm_rooms", {"_id": room_id})
        if room:
            if member_id in room.get("room_member_ids", []) or member_id in room.get("room_user_ids", []):
                data =  room.get("starred",[])
                if member_id in data:
                   return Response({"status":True}, status=status.HTTP_200_OK)
                return Response({"status":False}, status=status.HTTP_200_OK)
            return Response(data="User not in room", status=status.HTTP_404_NOT_FOUND)                     
        return Response("Invalid room", status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(["PUT"])
@db_init_with_credentials
def close_conversation(request, room_id, member_id):
    if request.method == "PUT":
        room = DB.read("dm_rooms", {"_id":room_id})
        if room or room is not None :
            room_users=room['room_user_ids']
            if member_id in room_users:
                room_users.remove(member_id)
                print(room_users)
                data = {'room_user_ids':room_users}
                print(data)
                response = DB.update("dm_rooms", room_id, data=data)
                return Response(response, status=status.HTTP_200_OK)
            return Response("You are not authorized", status=status.HTTP_401_UNAUTHORIZED)
        return Response("No Room / Invalid Room", status=status.HTTP_404_NOT_FOUND)
    return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)
