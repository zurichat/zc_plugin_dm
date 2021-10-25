import requests
from typing import Dict, List
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .db import *
from rest_framework.views import (
    APIView,
    exception_handler,
)
from django.core.files.storage import default_storage

# Import Read Write function to Zuri Core
from .resmodels import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from .centrifugo_handler import centrifugo_client
from rest_framework.pagination import PageNumberPagination
from .decorators import db_init_with_credentials
from .utils import SearchPagination
from asgiref.sync import sync_to_async
from django.views.decorators.cache import cache_page
# from django.http.response import JsonResponse


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
                return Response(data={"room_id" : response['room_id']}, status=response['status_code'])
        
        else:
            # print("            --------FAE-------              \n\r")
            user_ids = serializer.data["room_member_ids"]
            user_rooms = get_rooms(user_ids[0], DB.organization_id)
            if isinstance(user_rooms, list):
                for room in user_rooms:
                    room_users = room["room_user_ids"]
                    if set(room_users) == set(user_ids):
                        response_output = {
                                                "room_id": room["_id"]
                                            }
                        return Response(data=response_output, status=status.HTTP_200_OK)

            elif user_rooms is None:
                return Response("unable to read database", status=status.HTTP_424_FAILED_DEPENDENCY)

            elif user_rooms.get("status_code") != 404 or user_rooms.get("status_code") != 200:
                return Response("unable to read database", status=status.HTTP_424_FAILED_DEPENDENCY)
        
            fields = {"org_id": serializer.data["org_id"],
                      "room_user_ids": serializer.data["room_member_ids"],
                      "room_name": serializer.data["room_name"],
                      "private": serializer.data["private"],
                      "created_at": serializer.data["created_at"],
                      "bookmark": [],
                      "pinned": [],
                      "starred": [],
                      "closed": False
                          }

            response = DB.write("dm_rooms", data=fields)
            # ===============================

        if response.get("status") == 200:
            room_id = response.get("data").get("object_id")
            response_output = sidebar_emitter(org_id=DB.organization_id, member_id=member_id, group_room_name=serializer.data["room_name"])

            try:
                centrifugo_data = centrifugo_client.publish(
                    room=f"{DB.organization_id}_{member_id}_sidebar",
                    data=response_output,
                )  # publish data to centrifugo
                if centrifugo_data and centrifugo_data.get("status_code") == 200:
                    return Response(
                        data={"room_id":room_id,"message":"success"}, status=status.HTTP_201_CREATED
                    )
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
        return Response(f"unable to create room. Reason: {response}", status=status.HTTP_424_FAILED_DEPENDENCY)
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
    },
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
        if len(room_user_ids) >= 1:
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


@db_init_with_credentials
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
            if all_rooms and isinstance(all_rooms, list):
                for room_obj in all_rooms:
                    try:
                        room_members = room_obj['room_user_ids']
                        if len(room_members) > 2 and set(room_members) == set(user_ids):
                            response = {
                                "get_group_data": True,
                                "status_code": 200,
                                "room_id": room_obj["_id"]
                            }
                            return response
                    except KeyError:
                        pass

            fields = {
                "org_id": serializer.data["org_id"],
                "room_user_ids": serializer.data["room_member_ids"],
                "room_name": serializer.data["room_name"],
                "private": serializer.data["private"],
                "created_at": serializer.data["created_at"],
                "bookmark": [],
                "pinned": [],
                "starred": [],
                "closed": False
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
            if member_id in room.get("room_member_ids", []) or member_id in room.get(
                "room_user_ids", []
            ):
                data = room.get("starred", [])
                if member_id in data:
                    data.remove(member_id)
                else:
                    data.append(member_id)

                response = DB.update("dm_rooms", room_id,{"starred":data})

                if response and response.get("status_code",None) == None:
                    response_output = sidebar_emitter(org_id=DB.organization_id, member_id=member_id)
                    
                    try:
                        centrifugo_data = centrifugo_client.publish (
                            room=f"{DB.organization_id}_{member_id}_sidebar", data=response_output )  # publish data to centrifugo
                        if centrifugo_data and centrifugo_data.get ( "status_code" ) == 200:
                            return Response ( data={"message":"success"}, status=status.HTTP_201_CREATED )
                        else:
                            return Response(
                                data="starred status updated centrifugo unavailable",
                                status=status.HTTP_424_FAILED_DEPENDENCY,
                            )
                    except:
                        return Response(
                            data="centrifugo server not available",
                            status=status.HTTP_424_FAILED_DEPENDENCY,
                        )



                    # return Response(
                    #     "Success", status=status.HTTP_200_OK
                    #     )
                return Response(
                    data="Room not updated", status=status.HTTP_424_FAILED_DEPENDENCY
                )
            return Response(data="User not in room", status=status.HTTP_404_NOT_FOUND)
        return Response("Invalid room", status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        room = DB.read("dm_rooms", {"_id": room_id})
        if room:
            if member_id in room.get("room_member_ids", []) or member_id in room.get(
                "room_user_ids", []
            ):
                data = room.get("starred", [])
                if member_id in data:
                    return Response({"status": True}, status=status.HTTP_200_OK)
                return Response({"status": False}, status=status.HTTP_200_OK)
            return Response(data="User not in room", status=status.HTTP_404_NOT_FOUND)
        return Response("Invalid room", status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["post"],
    operation_summary="Adds a member to a room",
    responses={
        201: "Created",
        406: "Not Acceptable, You can only add users to a group dm",
        400: "Bad Request",
        424: "Failed Dependency",
    },
)
@api_view(["POST"])
@db_init_with_credentials
def group_member_add(request, room_id, member_id):
    """
    Adds a user to a group dm
    returns 201 response if succesful or the appropriate response otherwise

    :params: org id and room_id
    :payload: room_id: str, members_id: list & room_name: str
    """
    ORG_ID = DB.organization_id
    serializer = AddMemberSerializer(data=request.data)
    if serializer.is_valid():

        members_id = serializer.data['members_id']
        room_id = serializer.data['room_id']

        room = DB.read('dm_rooms', {"_id": room_id})
        if room and isinstance(room, dict):
            room_members = room['room_user_ids']
            
            room_creator = room_members[0]
            # print("ROOM CREATOR", room_creator)
            # print("ROOM MEMBERS BEFORE", room_members)

            if len(room_members) > 2:
                
                # if member_id not in room_members:
                    # room_members.append(member_id)
                    
                room_members.extend(members_id)
                room_members = list(set(room_members))
                
                if len(room_members) > 9:
                    return Response("Max Number For Members In a Group is 9", status=status.HTTP_400_BAD_REQUEST)
                # print("ROOM MEMBERS AFTER", room_members)                
                
                # =====================================================
                # =====================================================

                user_rooms = get_rooms(room_creator, DB.organization_id)
                if user_rooms and isinstance(user_rooms, list):
                    for room in user_rooms:
                        room_users = room["room_user_ids"]
                        if set(room_users) == set(room_members):
                            response_output = {
                                "room_id": room["_id"]
                            }
                            return Response(data=response_output, status=status.HTTP_200_OK)

                elif user_rooms.get("status_code") != 404:
                    if user_rooms is None or user_rooms.get("status_code") != 200:
                        return Response("unable to read database", status=status.HTTP_424_FAILED_DEPENDENCY)

                fields = {
                    "org_id": f"{ORG_ID}",
                    "room_user_ids": room_members,
                    "room_name": serializer.data["room_name"],
                    "private": serializer.data["private"],
                    "created_at": serializer.data["created_at"],
                    "bookmark": [],
                    "pinned": [],
                    "starred": [],
                    "closed": False
                }

                response = DB.write("dm_rooms", data=fields)
                # ===============================

                data_ID = response.get("data").get("object_id")
                if response.get("status") == 200:
                    response_output = {
                        "event": "sidebar_update",
                        "plugin_id": "dm.zuri.chat",
                        "data": {
                            "group_name": "DM",
                            "name": "DM Plugin",
                            "category": "direct messages",
                            "show_group": False,
                            "button_url": "/dm",
                            "public_rooms": [],
                            "joined_rooms": sidebar_emitter(org_id=DB.organization_id, member_id=room_creator, group_room_name=serializer.data["room_name"])
                        }
                    }

                    try:
                        centrifugo_data = centrifugo_client.publish(
                            room=f"{DB.organization_id}_{room_creator}_sidebar",
                            data=response_output)  # publish data to centrifugo
                        if centrifugo_data and centrifugo_data.get("status_code") == 200:
                            return Response(data=response_output, status=status.HTTP_201_CREATED)
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


                # =====================================================
                # =====================================================

            else:
                err_response = {"error": "Room is not a group room, Can only add users to group dm"}
                return Response(err_response, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response({"error": "Unable to read DB"}, status=status.HTTP_424_FAILED_DEPENDENCY)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(
    methods=["put"],
    operation_summary="Closes DM on the sidebar",
    responses={
        200: "success",
        404: "room not found",
        405: "Method Not Allowed",
        424: "failed",
    },
)
@api_view(["PUT"])
#@db_init_with_credentials
def close_conversation(request, org_id, room_id, member_id):
    """
    This function allows for the Closing of a DM room on the sidebar
    The params taken are the organization ID, room ID and the ID of the member initiating the command
    The HTTPS method is PUT
    A request to this function matches a valid room to a user in the room users list
    It then removes the room from the sidebar in realtime by toggling the closed status of the room from False to True
    """
    data = {}

    try:
        room = DB.read("dm_rooms", {"_id": room_id})
    except Exception:
        return None
    if room:
        if member_id in room["room_user_ids"]:
            if room["closed"] == False:
                data = {
                    "closed": True
                }                                           
            else:
                data = {
                    "closed": False
                }
            response = DB.update("dm_rooms", room_id, data) 
            if response:
                output_data = {
                            "event": "sidebar_update",
                            "plugin_id": "dm.zuri.chat",
                            "data": {
                                "name": "DM Plugin",
                                "description": "closes a DM conversation",
                                "group_name": "DM",
                                "category": "direct messages",
                                "show_group": False,
                                "button_url": "/dm",
                                "public_rooms": [],
                                "joined_rooms": sidebar_emitter(org_id=org_id, member_id=member_id),
                                "starred_rooms": []
                            }
                }                    
                try:
                    centrifugo_data = centrifugo_client.publish (
                        room=f"{org_id}_{member_id}_sidebar", data=output_data )
                    if centrifugo_data and centrifugo_data.get ( "status_code" ) == 200:
                        return Response ( data=output_data, status=status.HTTP_200_OK )
                    else:
                        return Response(
                            data="conversation closed but centrifugo unavailable",
                            status=status.HTTP_424_FAILED_DEPENDENCY,
                        )
                except:
                    return Response(
                        data="centrifugo server not available",
                        status=status.HTTP_424_FAILED_DEPENDENCY,
                    )
            else:
                return Response(
                        "failed, conversation not closed", status=status.HTTP_424_FAILED_DEPENDENCY
                    )
        return Response("member not in room", status=status.HTTP_403_FORBIDDEN)
    return Response("room not found or not in users list", status=status.HTTP_404_NOT_FOUND)



@swagger_auto_schema(
    methods=["get"],
    operation_summary="searches for message by a user",
    responses={404: "Error: Not Found"},
)
@sync_to_async
@api_view(["GET"])
@db_init_with_credentials
def search_DM(request, member_id):
    key = request.query_params.get("q", "")
    users = request.query_params.getlist("filter", [])
    limit = request.query_params.get("limit", 20)

    try:
        if type(limit) == str:
            limit = int(limit)
    except ValueError:
        limit = 20

    paginator = SearchPagination()
    paginator.page_size = limit

    try:
        if users != []:
            rooms_query = {
                "$and": [
                    {"room_user_ids": member_id},
                    {"room_user_ids": {"$in": users}},
                ]
            }
        else:
            rooms_query = {"room_user_ids": member_id}
            
        options = {"sort": {"created_at": -1},}
        rooms = DB.read_query("dm_rooms", query=rooms_query, options=options)
        
        org_id = DB.organization_id
        room_ids = list(map(lambda room: room["_id"], rooms)) if rooms else []
        
        if rooms:
            members = get_all_organization_members(org_id)
            messages_query = {
                "$and":[
                    {"message":{"$regex":key}},
                    {"room_id":{"$in":room_ids}}
                ]
            }
            
            messages = DB.read_query("dm_messages", query = messages_query)
            if messages:
            
                members_found = {}
                for message in messages:
                    if message['sender_id'] not in members_found:
                        members_found[message['sender_id']] = get_member(members,message.get('sender_id')) #get profile
                    
                    if 'read' in message.keys(): del message['read']
                    if 'pinned' in message.keys():del message['pinned']
                    if 'saved_by' in message.keys():del message['saved_by']
                    if 'threads' in message.keys(): del message['threads']
                    if 'thread' not in message.keys(): message['thread'] = False 
                    if 'notes' in  message.keys(): del message['notes']
                    if 'replied_message' in  message.keys(): del message['replied_message']
                    if 'sent_from_thread' in message.keys(): del message['sent_from_thread']
                    if 'reactions' in message.keys(): del message['reactions']
                    if 'thread' in message.keys(): del message['thread']
                    
                    message['destination_url'] = f"/dm/{message['room_id']}"
                    message['room_name'] =  members_found[message['sender_id']]['user_name'] if members_found[message['sender_id']] else None
                    message['title'] =  members_found[message['sender_id']]['user_name'] if members_found[message['sender_id']] else None
                    message['created_by'] = members_found[message['sender_id']]['user_name'] if members_found[message['sender_id']] else None
                    message['images_url'] = [members_found[message['sender_id']]['image_url'] if members_found[message['sender_id']] else None]
                    message['content'] = message['message']
                    
                result = paginator.paginate_queryset(messages, request)
                return paginator.get_paginated_response(result,key,users,request)
        
                
        result = paginator.paginate_queryset([], request)
        return paginator.get_paginated_response(result,key,users,request)
        
    except Exception as e:
        print(e)
        result = paginator.paginate_queryset([], request)
        return paginator.get_paginated_response(result,key,users,request)
    
@swagger_auto_schema(
    methods=["get"],
    operation_summary="gets search suggestion for a user",
    responses={404: "Error: Not Found"},
)
@sync_to_async
@api_view(["GET"])
@db_init_with_credentials
def search_suggestions(request, member_id):
    query = {"room_user_ids":member_id}
    options = {
        "sort":{"created_at": -1},
        "projection":{"room_user_ids":1, "_id":0}
    }
    data = {}
    org_id = DB.organization_id
    try:
        members = get_all_organization_members(org_id)
        rooms = DB.read_query("dm_rooms",query=query,options=options)
        member_ids = []
        if rooms:    
            for room in rooms:
                room['room_user_ids'].remove(member_id)
                if None in room['room_user_ids']:
                    room['room_user_ids'].remove(None)
                member_ids.extend(room['room_user_ids'])
                
        for member in members:
            if member['_id'] in member_ids:
                username = member.get('user_name')
                data[member['_id']] = username
                
        response = {
            "status":"ok",
            "type":"suggestions",
            "data":data
        }
                   
    except Exception as e:
        print(e)     
        response = {
            "status":"ok",
            "type":"suggestions",
            "data":data
        }
    return Response(response, status=status.HTTP_200_OK)


@sync_to_async
@api_view(["GET"])
@db_init_with_credentials
def all_dms(request, member_id):
    """
    Retrieves the all latest dm in a room that the user had been active and
    also retrives the latest messages in the displayed dms.
    """
    if request.method =="GET":
        paginator = PageNumberPagination()
        paginator.page_size = 20
        rooms=DB.read_query("dm_rooms", query = {"room_user_ids":member_id} )
    
        all_messages=[] #holds data to render
        try:
            room_ids = [room['_id'] for room in rooms ]
            
            query = {
                "room_id":{"$in":room_ids}
            }
            
            options = {
                "sort":{'created_at': -1}
            }
            
            messages=DB.read_query("dm_messages", query=query, options = options)

            for message in messages:
                if message['room_id'] in room_ids:
                    all_messages.append(message)
                    room_ids.remove(message['room_id'])
                        
            response = paginator.paginate_queryset(all_messages, request)
            return paginator.get_paginated_response(response)
        
        except:
            response = paginator.paginate_queryset(all_messages, request)
            return paginator.get_paginated_response(response)

