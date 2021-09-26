import json
import uuid
import re
from django.http import response
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import generic
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework import status
import requests, time
from .db import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.core.files.storage import default_storage

# Import Read Write function to Zuri Core
from .resmodels import *
from .serializers import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .utils import SendNotificationThread
from datetime import datetime
import datetime as datetimemodule


from .centrifugo_handler import centrifugo_client
from rest_framework.pagination import PageNumberPagination

from .decorators import db_init_with_credentials


def index(request):
    context = {}
    return render(request, "index.html", context)


# Shows basic information about the DM plugin
def info(request):
    info = {
        "message": "Plugin Information Retrieved",
        "data": {
            "type": "Plugin Information",
            "plugin_info": {
                "name": "DM Plugin",
                "description": [
                    "Zuri.chat plugin",
                    "DM plugin for Zuri Chat that enables users to send messages to each other",
                ],
            },
            "scaffold_structure": "Monolith",
            "team": "HNG 8.0/Team Orpheus",
            "sidebar_url": "https://dm.zuri.chat/api/v1/sidebar",
            "homepage_url": "https://dm.zuri.chat/",
            "create_room_url":"https://dm.zuri.chat/api/v1/<str:org_id>/createroom"
        },
        "success": "true",
    }

    return JsonResponse(info, safe=False)


def verify_user(token):
    """
    Call Endpoint for verification of user (sender)
    It takes in either token or cookies and returns a python dictionary of
    user info if 200 successful or 401 unathorized if not
    """
    url = "https://api.zuri.chat/auth/verify-token"

    headers = {}
    if "." in token:
        headers["Authorization"] = f"Bearer {token}"
    else:
        headers["Cookie"] = token

    response = requests.get(url, headers=headers)
    response = response.json()

    return response


# Returns the json data of the sidebar that will be consumed by the api
# The sidebar info will be unique for each logged in user
# user_id will be gotten from the logged in user
# All data in the message_rooms will be automatically generated from zuri core


def side_bar(request):
    org_id = request.GET.get("org", None)
    user = request.GET.get("user", None)
    user_rooms = get_rooms(user_id=user, org_id=org_id)
    rooms = []
    
    for room in user_rooms:
        if "org_id" in room:
            if org_id == room["org_id"]:
                room_profile={}
                for user_id in room["room_user_ids"]:
                    profile = get_user_profile(org_id,user_id)
                    if profile["status"]==200:
                        room_profile["room_name"] = profile["data"]["user_name"]
                        room_profile["room_image"] = "https://cdn.iconscout.com/icon/free/png-256/account-avatar-profile-human-man-user-30448.png"
                        rooms.append(room_profile)
                room_profile["room_url"] = f"/dm/{org_id}/{room['_id']}"
    side_bar = {
        "name": "DM Plugin",
        "description": "Sends messages between users",
        "plugin_id": "6135f65de2358b02686503a7",
        "organisation_id": f"{org_id}",
        "user_id": f"{user}",
        "group_name": "DM",
        "show_group": False,
        "public_rooms": [],
        "joined_rooms": rooms,
        # List of rooms/collections created whenever a user starts a DM chat with another user
        # This is what will be displayed by Zuri Main
    }
    return JsonResponse(side_bar, safe=False)


@swagger_auto_schema(
    methods=["post"],
    request_body=MessageSerializer,
    responses={
        201: MessageResponse,
        400: "Error: Bad Request"
    }
)
@api_view(["POST"])
@db_init_with_credentials
def send_message(request, room_id):
    """
    Sends messages to users in rooms.
    It checks if room already exist before sending data.
    It makes a publish event to centrifugo after data
    is persisted
    """
    request.data["room_id"] = room_id
    print(request)
    serializer = MessageSerializer(data=request.data)

    if serializer.is_valid():
        data = serializer.data
        room_id = data["room_id"]  # room id gotten from client request

        room = DB.read("dm_rooms", {"_id": room_id})
        if room and room.get('status_code', None) == None:
            if data["sender_id"] in room.get("room_user_ids", []):

                response = DB.write("dm_messages", data=serializer.data)
                if response.get("status", None) == 200:

                    response_output = {
                        "status": response["message"],
                        "event": "message_create",
                        "message_id": response["data"]["object_id"],
                        "room_id": room_id,
                        "thread": False,
                        "data": {
                            "sender_id": data["sender_id"],
                            "message": data["message"],
                            "created_at": data["created_at"],
                        }
                    }
                    try:
                        centrifugo_data = centrifugo_client.publish(
                            room=room_id, data=response_output)  # publish data to centrifugo
                        if centrifugo_data and centrifugo_data.get("status_code") == 200:
                            return Response(data=response_output, status=status.HTTP_201_CREATED)
                        else:
                            return Response(data="message not sent", status=status.HTTP_424_FAILED_DEPENDENCY)
                    except:
                        return Response(data="centrifugo server not available", status=status.HTTP_424_FAILED_DEPENDENCY)
                return Response(data="message not saved and not sent", status=status.HTTP_424_FAILED_DEPENDENCY)
            return Response("sender not in room", status=status.HTTP_400_BAD_REQUEST)
        return Response("room not found", status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["post"],
    request_body=ThreadSerializer,
    responses={
        201: ThreadResponse,
        400: "Error: Bad Request"
    }
)
@api_view(["POST"])
@db_init_with_credentials
def send_thread_message(request, room_id, message_id):
    """
    validates if the message exists, then sends
    a publish event to centrifugo after
    thread message is persisted.
    """
    request.data["message_id"] = message_id
    serializer = ThreadSerializer(data=request.data)

    if serializer.is_valid():
        data = serializer.data
        message_id = data["message_id"]
        sender_id = data["sender_id"]

        message = DB.read(
            "dm_messages", {"_id": message_id, "room_id": room_id}
        )  # fetch message from zc

        if message and message.get('status_code', None) == None:
            threads = message.get("threads", [])  # get threads
            del data["message_id"]  # remove message id from request to zc core
            # assigns an id to each message in thread
            data["_id"] = str(uuid.uuid1())
            threads.append(data)  # append new message to list of thread

            room = DB.read("dm_rooms", {"_id": message["room_id"]})
            if sender_id in room.get("room_user_ids", []):

                response = DB.update("dm_messages", message["_id"], {
                                     "threads": threads})  # update threads in db
                if response and response.get("status", None) == 200:

                    response_output = {
                        "status": response["message"],
                        "event": "thread_message_create",
                        "thread_id": data["_id"],
                        "room_id": message["room_id"],
                        "message_id": message["_id"],
                        "thread": True,
                        "data": {
                            "sender_id": data["sender_id"],
                            "message": data["message"],
                            "created_at": data["created_at"],
                        }
                    }

                    try:
                        centrifugo_data = centrifugo_client.publish(
                            room=room_id, data=response_output)  # publish data to centrifugo
                        if centrifugo_data and centrifugo_data.get("status_code") == 200:
                            return Response(data=response_output, status=status.HTTP_201_CREATED)
                        else:
                            return Response(data="message not sent", status=status.HTTP_424_FAILED_DEPENDENCY)
                    except:
                        return Response(data="centrifugo server not available", status=status.HTTP_424_FAILED_DEPENDENCY)
                return Response("data not sent", status=status.HTTP_424_FAILED_DEPENDENCY)
            return Response("sender not in room", status=status.HTTP_404_NOT_FOUND)
        return Response("message or room not found", status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["post"],
    request_body=RoomSerializer,
    responses={
        201: CreateRoomResponse,
        400: "Error: Bad Request"
    }
)
@api_view(["POST"])
@db_init_with_credentials
def create_room(request):
    """
    Creates a room between users.
    It takes the id of the users involved, sends a write request to the database .
    Then returns the room id when a room is successfully created
    """

    # validate request
    #   if 'Authorization' in request.headers:
    #       token = request.headers['Authorization']
    #   else:
    #       token = request.headers['Cookie']

    #   verify = verify_user(token)
    #   if verify.get("status") == 200:

    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        user_ids = serializer.data["room_user_ids"]
        user_rooms = get_rooms(user_ids[0], DB.organization_id)
        for room in user_rooms:
            room_users = room["room_user_ids"]
            if set(room_users) == set(user_ids):
                response_output = {"room_id": room["_id"]}
                return Response(data=response_output, status=status.HTTP_200_OK)
    response = DB.write("dm_rooms", data=serializer.data)
    data = response.get("data").get("object_id")
    if response.get("status") == 200:
        response_output = {"room_id": data}
        return Response(data=response_output, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["get"],
    query_serializer=UserRoomsSerializer,
    responses={400: "Error: Bad Request"},
)
@api_view(["GET"])
@db_init_with_credentials
def getUserRooms(request, user_id):
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
    query_serializer=GetMessageSerializer,
    responses={
        201: MessageResponse,
        400: "Error: Bad Request"
    }
)
@api_view(["GET"])
@db_init_with_credentials
def room_messages(request, room_id):
    """
    Retrieves messages in a room using a room id.
    It returns a 204 status code if there is no message in the room.
    The messages can be filter by adding date in the query,
    it also returns a 204 status if there are no messages.
    """
    if request.method == "GET":
        paginator = PageNumberPagination()
        paginator.page_size = 30
        date = request.GET.get("date", None)
        params_serializer = GetMessageSerializer(data=request.GET.dict())
        if params_serializer.is_valid():
            room = DB.read("dm_rooms", {"_id": room_id})
            if room:
                messages = get_room_messages(room_id, DB.organization_id)
                if date != None:
                    messages_by_date = get_messages(messages, date)
                    if messages_by_date == None or "message" in messages_by_date:
                        return Response(
                            data="No messages available",
                            status=status.HTTP_204_NO_CONTENT,
                        )
                    messages_page = paginator.paginate_queryset(
                        messages_by_date, request
                    )
                    return paginator.get_paginated_response(messages_page)
                else:
                    if messages == None or "message" in messages:
                        return Response(
                            data="No messages available",
                            status=status.HTTP_204_NO_CONTENT,
                        )
                    result_page = paginator.paginate_queryset(
                        messages, request)
                    return paginator.get_paginated_response(result_page)
            return Response(data="No such room", status=status.HTTP_400_BAD_REQUEST)
        return Response(params_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["get"],
    query_serializer=RoomInfoSerializer,
    responses={
        201: RoomInfoResponse,
        400: "Error: Bad Request"
    }
)
@api_view(["GET"])
@db_init_with_credentials
def room_info(request):
    """
    Retrieves information about a room.
    It takes the room id as a query param and searches the dm_rooms collection
    If the room exists, a json response of the room details is returned
    Else a 404 response is returned with a "No such room" message
    """
    room_id = request.GET.get("room_id", None)
    # org_id = request.GET.get("org_id", None)
    room_collection = "dm_rooms"
    rooms = DB.read(room_collection)
    print(rooms)
    if rooms is not None:
        for current_room in rooms:
            if current_room["_id"] == room_id:
                if "room_user_ids" in current_room:
                    room_user_ids = current_room["room_user_ids"]
                else:
                    room_user_ids = ""
                if "created_at" in current_room:
                    created_at = current_room["created_at"]
                else:
                    created_at = ""
                if "org_id" in current_room:
                    org_id = current_room["org_id"]
                else:
                    org_id = ""
                if len(room_user_ids) > 3:
                    text = f" and {len(room_user_ids)-2} others"
                elif len(room_user_ids) == 3:
                    text = "and 1 other"
                else:
                    text = " only"
                room_data = {
                    "room_id": room_id,
                    "org_id": org_id,
                    "room_user_ids": room_user_ids,
                    "created_at": created_at,
                    "description": f"This room contains the coversation between {room_user_ids[0]} and {room_user_ids[1]}{text}",
                    "Number of users": f"{len(room_user_ids)}",
                }
                return Response(data=room_data, status=status.HTTP_200_OK)
        return Response(data="No such Room", status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# /code for updating room
@api_view(["GET", "POST"])
@db_init_with_credentials
def edit_room(request, pk):
    """
    This is used to update message context using message id as identifier,
    first --> we check if this message exist, if it does not exist we raise message doesnot exist,
    if above message exists:
        pass GET request to view the message one whats to edit.
        or pass POST with data to update

    """
    try:
        message = DB.read("dm_messages", {"id": pk})
    except:
        return JsonResponse(
            {"message": "The room does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        singleRoom = DB.read("dm_messages", {"id": pk})
        return JsonResponse(singleRoom)
    else:
        room_serializer = MessageSerializer(
            message, data=request.data, partial=True)
        if room_serializer.is_valid():
            room_serializer.save()
            data = room_serializer.data
            # print(data)
            response = DB.update("dm_messages", pk, data)
            return Response(room_serializer.data)
        return Response(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(data="No Rooms", status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["get"], 
    responses={
        201: MessageLinkResponse, 
        400: "Error: Bad Request"
    }
)
@api_view(["GET"])
@db_init_with_credentials
def copy_message_link(request, message_id):
    """
    Retrieves a single message using a message_id as query params.
    If message_id is provided, it returns a dictionary with information about the message,
    or a 204 status code if there is no message with the same message id.
    The message information returned is used to generate a link which contains a room_id and a message_id
    """
    if request.method == "GET":
        message = DB.read("dm_messages", {"id": message_id})
        room_id = message["room_id"]
        message_info = {
            "room_id": room_id,
            "message_id": message_id,
            "link": f"https://dm.zuri.chat/getmessage/{room_id}/{message_id}",
        }
        return Response(data=message_info, status=status.HTTP_200_OK)
    else:
        return JsonResponse(
            {"message": "The message does not exist"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
@db_init_with_credentials
def read_message_link(request, room_id, message_id):
    """
    This is used to retrieve a single message. It takes a message_id as query params.
    or a 204 status code if there is no message with the same message id.
    I will use the message information returned to generate a link which contains a room_id and a message_id
    """

    if request.method == "GET":
        message = DB.read(
            "dm_messages", {"id": message_id, "room_id": room_id})
        return Response(data=message, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'message': 'The message does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@db_init_with_credentials
def get_links(request, room_id):
    """
    Search messages in a room and return all links found
    Accepts room id as a param and queries the dm_messages collection for links attached to that id
    If no links were found, a 404 is returned
    """
    url_pattern = r"^(?:ht|f)tp[s]?://(?:www.)?.*$"
    regex = re.compile(url_pattern)
    matches = []
    messages = DB.read("dm_messages", filter={"room_id": room_id})
    if messages is not None:
        for message in messages:
            for word in message.get("message").split(" "):
                match = regex.match(word)
                if match:
                    matches.append(
                        {"link": str(word), "timestamp": message.get(
                            "created_at")}
                    )
        data = {"links": matches, "room_id": room_id}
        return Response(data=data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    methods=["post"],
    request_body=BookmarkSerializer,
    responses={400: "Error: Bad Request"}
)
@api_view(["POST"])
@db_init_with_credentials
def save_bookmark(request, room_id):
    """
    Saves a link as a bookmark in a room
    It takes a room id as param and queries the dm_rooms collection
    Once room is found, it saves the link in the room as a list in the bookmark document
    """
    try:
        serializer = BookmarkSerializer(data=request.data)
        room = DB.read("dm_rooms", {"id": room_id})
        bookmarks = room["bookmarks"] or []
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
    if serializer.is_valid() and bookmarks is not None:
        bookmarks.append(serializer.data)
        data = {"bookmarks": bookmarks}
        response = DB.update("dm_rooms", room_id, data=data)
        if response.get("status") == 200:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["post"],
    request_body=CookieSerializer,
    responses={400: "Error: Bad Request"},
)
@api_view(["GET", "POST"])
@db_init_with_credentials
def organization_members(request):
    """
    Retrieves a list of all members in an organization.
    :returns: json response -> a list of objects (members) or 401_Unauthorized messages.

    GET: simulates production - if request is get, either token or cookie gotten from FE will be used,
    and authorization should take places automatically.

    POST: simulates testing - if request is post, send the cookies through the post request, it would be added
    manually to grant access, PS: please note cookies expire after a set time of inactivity.
    """
    ORG_ID = DB.organization_id
    
    url = f"https://api.zuri.chat/organizations/{ORG_ID}/members"

    if request.method == "GET":
        headers = {}

        if "Authorization" in request.headers:
            headers["Authorization"] = request.headers["Authorization"]
        else:
            headers["Cookie"] = request.headers["Cookie"]

        response = requests.get(url, headers=headers)

    elif request.method == "POST":
        cookie_serializer = CookieSerializer(data=request.data)

        if cookie_serializer.is_valid():
            cookie = cookie_serializer.data["cookie"]
            response = requests.get(url, headers={"Cookie": cookie})
        else:
            return Response(
                cookie_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    if response.status_code == 200:
        response = response.json()["data"]
        return Response(response, status=status.HTTP_200_OK)
    return Response(response.json(), status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    methods=["get"],
    responses={
        200: BookmarkResponse,
        400: "Error: Bad Request"
    }
)
@api_view(["GET"])
@db_init_with_credentials
def retrieve_bookmarks(request, room_id):
    """
    This endpoint retrieves all saved bookmarks in the room
    It takes a room id as param and queries the dm_rooms collection
    Once room is found, it retrieves all the bookmarked links in the room
    It then returns a json output of the links in a list
    """
    try:
        room = DB.read("dm_rooms", {"id": room_id})
        bookmarks = room["bookmarks"] or []
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
    if bookmarks is not None:
        serializer = BookmarkSerializer(data=bookmarks, many=True)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
@db_init_with_credentials
def mark_read(request, message_id):
    """
    Marks a message as read and unread
    Queries the dm_messages collection using a unique message id
    Checks read status of the message and updates the collection
    """
    try:
        message = DB.read("dm_messages", {"id": message_id})
        read = message["read"]
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
    data = {"read": not read}
    response = DB.update("dm_messages", message_id, data=data)
    message = DB.read("dm_messages", {"id": message_id})

    if response.get("status") == 200:
        return Response(data=data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["put"],
    responses={
        200: PinMessageResponse, 
        400: "Error: Bad Request"
    }
)
@api_view(["PUT"])
@db_init_with_credentials
def pinned_message(request, message_id):
    """
    This is used to pin a message.
    The message_id is passed to it which
    reads through the database, gets the room id,
    generates a link and then add it to the pinned key value.

    If the link already exist, it would greet you with a nice response from the developer that wrote it.
    """
    try:
        message = DB.read("dm_messages", {"id": message_id})
        print("message", message)
        room_id = message["room_id"]
        print("room id", room_id)
        room = DB.read("dm_rooms", {"id": room_id})
        print("room", room)
        pin = room["pinned"] or []
        print("pin", pin)
        link = f"https://dm.zuri.chat/api/v1/{room_id}/{message_id}/pinnedmessage"
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
    if link not in pin:
        pin.append(link)
        data = {"pinned": pin}
        response = DB.update("dm_rooms", room_id, data)
        room = DB.read("dm_rooms", {"id": room_id})
        if response.get("status") == 200:
            return Response(data=room, status=status.HTTP_200_OK)
    return Response(
        data="Already exist! why do you want to break my code?",
        status=status.HTTP_409_CONFLICT,
    )


@swagger_auto_schema(
    methods=["delete"],
    responses={
        200: UnpinMessageResponse, 
        400: "Error: Bad Request"
    }
)
@api_view(["DELETE"])
@db_init_with_credentials
def delete_pinned_message(request, message_id):
    """
    This is used to delete a pinned message.
    It takes in the message id, gets the room id, generates a link and then check
    if that link exists. If it exists, it deletes it
    if not it returns a 400 status response
    """
    try:
        message = DB.read("dm_messages", {"id": message_id})
        room_id = message["room_id"]
        room = DB.read("dm_rooms", {"id": room_id})
        pin = room["pinned"] or []
        link = f"https://dm.zuri.chat/api/v1/{room_id}/{message_id}/pinnedmessage"
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
    if link in pin:
        print("YES")
        pin.remove(link)
        data = {"pinned": pin}
        response = DB.update("dm_rooms", room_id, data)
        room = DB.read("dm_rooms", {"id": room_id})
        if response.get("status") == 200:
            return Response(data=data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["get"],
    responses={
        200: FilterMessageResponse, 
        400: "Error: No such room or invalid Room"
    }
)
@api_view(["GET"])
@db_init_with_credentials
def message_filter(request, room_id):
    """
    Fetches all the messages in a room, and sort it out according to time_stamp.
    """
    if request.method == "GET":
        room = DB.read("dm_rooms", {"id": room_id})
        # room = "613b2db387708d9551acee3b"

        if room is not None:
            all_messages = DB.read("dm_messages", filter={"room_id": room_id})
            if all_messages is not None:
                message_timestamp_filter = sorted(
                    all_messages, key=lambda k: k["created_at"]
                )
                return Response(message_timestamp_filter, status=status.HTTP_200_OK)
            return Response(
                data="No messages available", status=status.HTTP_204_NO_CONTENT
            )
        return Response(
            data="No Room or Invalid Room", status=status.HTTP_400_BAD_REQUEST
        )


# @swagger_auto_schema(
#     methods=["delete"],
#     request_body=DeleteMessageSerializer,
#     responses={400: "Error: Bad Request"},
# )
# # @api_view(["DELETE"])
# # @db_init_with_credentials
# # def delete_message(request):
# #     """
# #     Deletes a message after taking the message id
# #     """

# #     if request.method == "DELETE":
# #         message_id = request.GET.get("message_id")
# #         message = DB.read("dm_messages", {"_id": message_id})
# #         if message:
# #             response = DB.delete("dm_messages", message_id)
# #             return Response(response, status.HTTP_200_OK)
# #         else:
# #             return Response("No such message", status.HTTP_404_NOT_FOUND)
# #     return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@swagger_auto_schema(
    methods=["get"],
    responses={
        201: UserProfileResponse,
        400: "Error: Bad Request"
    }
)
@api_view(["GET"])
def user_profile(request, org_id, member_id):
    """
    Retrieves the user details of a member in an organization using a unique user_id
    If request is successful, a json output of select user details is returned
    Elif login session is expired or wrong details were entered, a 401 response is returned
    Else a 405 response returns if a wrong method was used
    """
    url = f"https://api.zuri.chat/organizations/{org_id}/members/{member_id}"

    if request.method == "GET":
        headers = {}

        if "Authorization" in request.headers:
            headers["Authorization"] = request.headers["Authorization"]
        else:
            headers["Cookie"] = request.headers["Cookie"]

        response = requests.get(url, headers=headers)

    # elif request.method == "POST":
    #     cookie_serializer = CookieSerializer(data=request.data)

    #     if cookie_serializer.is_valid():
    #         cookie = cookie_serializer.data["cookie"]
    #         response = requests.get(url, headers={"Cookie": cookie})
    #     else:
    #         return Response(
    #             cookie_serializer.errors, status=status.HTTP_400_BAD_REQUEST
    #         )

    if response.status_code == 200:
        data = response.json()["data"]
        output = {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "display_name": data["display_name"],
            "bio": data["bio"],
            "pronouns": data["pronouns"],
            "email": data["email"],
            "phone": data["phone"],
            "status": data["status"],
        }
        return Response(output, status=status.HTTP_200_OK)
    return Response(response.json(), status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    methods=["post"],
    request_body=ReminderSerializer,
    responses={400: "Error: Bad Request"}
)
@api_view(["POST"])
@db_init_with_credentials
def remind_message(request):
    """
        This is used to remind a user about a  message
        Your body request should have the format
        {
        "mesage_id": "33",
        "current_date": "Tue, 22 Nov 2011 06:00:00 GMT",
        "scheduled_date":"Tue, 22 Nov 2011 06:00:00 GMT"
    }
    """
    serializer = ReminderSerializer(data=request.data)
    if serializer.is_valid():
        serialized_data = serializer.data
        message_id = serialized_data['message_id']
        current_date = serialized_data['current_date']
        scheduled_date = serialized_data['scheduled_date']
        notes_data = serialized_data['notes']
        # calculate duration and send notification
        local_scheduled_date = datetime.strptime(
            scheduled_date, '%a, %d %b %Y %H:%M:%S %Z')
        utc_scheduled_date = local_scheduled_date.replace(tzinfo=timezone.utc)

        local_current_date = datetime.strptime(
            current_date, '%a, %d %b %Y %H:%M:%S %Z')
        utc_current_date = local_current_date.replace(tzinfo=timezone.utc)
        duration = local_scheduled_date - local_current_date
        duration_sec = duration.total_seconds()
        if duration_sec > 0:
            # get message infos , sender info and recpient info
            message = DB.read("dm_messages", {"id": message_id})
            if message:
                room_id = message['room_id']
                try:
                    room = DB.read("dm_rooms", {"_id": room_id})

                except Exception as e:
                    print(e)
                    return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

                users_in_a_room = room.get("room_user_ids", []).copy()
                message_content = message['message']
                sender_id = message['sender_id']
                recipient_id = ''
                if sender_id in users_in_a_room:
                    users_in_a_room.remove(sender_id)
                    recipient_id = users_in_a_room[0]
                response_output = {
                    "recipient_id": recipient_id,
                    "sender_id": sender_id,
                    "message": message_content,
                    "scheduled_date": scheduled_date
                }
                if notes_data is not None:
                    try:
                        notes = message["notes"] or []
                        notes.append(notes_data)
                        response = DB.update(
                            "dm_messages", message_id, {"notes": notes})
                    except Exception as e:
                        notes = []
                        notes.append(notes_data)
                        response = DB.update(
                            "dm_messages", message_id, {"notes": notes})
                    if response.get("status") == 200:
                        response_output["notes"] = notes
                        return Response(data=response_output, status=status.HTTP_201_CREATED)
                SendNotificationThread(
                    duration, duration_sec, utc_scheduled_date, utc_current_date,).start()
                return Response(data=response_output, status=status.HTTP_201_CREATED)
            return Response(data="No such message", status=status.HTTP_400_BAD_REQUEST)
        return Response(data="Your current date is ahead of the scheduled time. Are you plannig to go back in time?", status=status.HTTP_400_BAD_REQUEST)
    return Response(data="Bad Format ", status=status.HTTP_400_BAD_REQUEST)


class SendFile(APIView):
    """
    This endpoint is a send message endpoint that can take files, upload them 
    and return the urls to the uploaded files to the media list in the message 
    serializer
    This endpoint uses form data
    The file must be passed in with the key "file"

    """

    parser_classes = (MultiPartParser, FormParser)

    # @method_decorator(db_init_with_credentials)
    def post(self, request, room_id, org_id):
        print(request.FILES)
        if request.FILES:
            file_urls = []
            files = request.FILES.getlist('file')
            if len(files) == 1:
                for file in request.FILES.getlist('file'):
                    file_data = DB.upload(file)
                    if file_data["status"] == 200:
                        for datum in file_data["data"]['files_info']:
                            file_urls.append(datum['file_url'])
                    else:
                        return Response(file_data)
            elif len(files) > 1:
                multiple_files = []
                for file in files:
                    multiple_files.append(("file", file))
                file_data = DB.upload_more(multiple_files)
                if file_data["status"] == 200:
                    for datum in file_data["data"]['files_info']:
                        file_urls.append(datum['file_url'])
                else:
                    return Response(file_data)

            request.data["room_id"] = room_id
            print(request)
            serializer = MessageSerializer(data=request.data)

            if serializer.is_valid():
                data = serializer.data
                room_id = data["room_id"]  # room id gotten from client request

                room = DB.read("dm_rooms", {"_id": room_id})
                if room:
                    if data["sender_id"] in room.get("room_user_ids", []):
                        data["media"] = file_urls
                        response = DB.write("dm_messages", data=data)
                        if response.get("status", None) == 200:

                            response_output = {
                                "status": response["message"],
                                "event": "message_create",
                                "message_id": response["data"]["object_id"],
                                "room_id": room_id,
                                "thread": False,
                                "data": {
                                    "sender_id": data["sender_id"],
                                    "message": data["message"],
                                    "created_at": data["created_at"],
                                    "media": data["media"],
                                },
                            }

                            centrifugo_data = send_centrifugo_data(
                                room=room_id, data=response_output
                            )  # publish data to centrifugo
                            # print(centrifugo_data)
                            if centrifugo_data["message"].get("error", None) == None:
                                return Response(
                                    data=response_output, status=status.HTTP_201_CREATED
                                )
                        return Response(
                            data="data not sent",
                            status=status.HTTP_424_FAILED_DEPENDENCY,
                        )
                    return Response(
                        "sender not in room", status=status.HTTP_400_BAD_REQUEST
                    )
                return Response("room not found", status=status.HTTP_404_NOT_FOUND)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(
            "No file attached, Use send Message api to send only a message",
            status=status.HTTP_204_NO_CONTENT,
        )


class Emoji(APIView):
    """
    List all Emoji reactions, or create a new Emoji reaction.
    """

    @swagger_auto_schema(
        responses={400: "Error: Bad Request"},
    )
    @method_decorator(db_init_with_credentials)
    def get(self, request, room_id: str, message_id: str):
        # fetch message related to that reaction
        message = DB.read(
            "dm_messages", {"_id": message_id, "room_id": room_id})
        if message:
            print(message)
            if response:
                return Response(
                    data={
                        "status": message["message"],
                        "event": "get_message_reactions",
                        "room_id": message["room_id"],
                        "message_id": message["_id"],
                        "data": {
                            "reactions": message["reactions"],
                        },
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                data="Data not retrieved", status=status.HTTP_424_FAILED_DEPENDENCY
            )
        return Response("No such message or room", status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=EmojiSerializer,
        responses={400: "Error: Bad Request"},
    )
    @method_decorator(db_init_with_credentials)
    def post(self, request, room_id: str, message_id: str):
        request.data["message_id"] = message_id
        serializer = EmojiSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            data["count"] += 1
            message_id = data["message_id"]
            sender_id = data["sender_id"]

            # fetch message related to that reaction
            message = DB.read(
                "dm_messages", {"_id": message_id, "room_id": room_id})
            if message:
                # get reactions
                reactions = message.get("reactions", [])
                reactions.append(data)

                room = DB.read(ROOMS, {"_id": message["room_id"]})
                if room:
                    # update reactions for a message
                    response = DB.update(MESSAGES, message_id, {
                                         "reactions": reactions})
                    if response.get("status", None) == 200:
                        response_output = {
                            "status": response["message"],
                            "event": "add_message_reaction",
                            "reaction_id": str(uuid.uuid1()),
                            "room_id": message["room_id"],
                            "message_id": message["_id"],
                            "data": {
                                "sender_id": sender_id,
                                "reaction": data["data"],
                                "created_at": data["created_at"],
                            },
                        }
                        centrifugo_data = centrifugo_client.publish(
                            room=message["room_id"], data=response_output
                        )  # publish data to centrifugo
                        if centrifugo_data["message"].get("error", None) == None:
                            return Response(
                                data=response_output, status=status.HTTP_201_CREATED
                            )
                    return Response(
                        "Data not sent", status=status.HTTP_424_FAILED_DEPENDENCY
                    )

                return Response("Unknown room", status=status.HTTP_404_NOT_FOUND)
            return Response(
                "Message or room not found", status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
        )


# @swagger_auto_schema(
    # methods=["post"],
    # request_body=ScheduleMessageSerializer,
    # responses={400: "Error: Bad Request"},
# )
@api_view(["POST"])
@db_init_with_credentials
def scheduled_messages(request):
    ORG_ID = DB.organization_id
    
    schedule_serializer = ScheduleMessageSerializer(data=request.data)
    if schedule_serializer.is_valid():
        data = schedule_serializer.data
        
        sender_id = data["sender_id"]
        room_id = data["room_id"]
        message = data["message"]
        timer = data["timer"]
        
        now = datetime.now()
        timer = datetime.strptime(timer, '%Y-%m-%d %H:%M:%S')
        duration = timer - now
        duration = duration.total_seconds()
        
        url = f"https://dm.zuri.chat/api/v1/org/{ORG_ID}/rooms/{room_id}/messages"
        payload = json.dumps({
            "sender_id": f"{sender_id}",
            "room_id": f"{room_id}",
            "message": f"{message}",
        })
        headers = {
            'Content-Type': 'application/json'
        }
        time.sleep(duration)
        response = requests.request("POST", url, headers=headers, data=payload)
    else:
        return Response(schedule_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if response.status_code == 201:
        return Response(response.json(), status=status.HTTP_201_CREATED)
    return Response(response.json(), status=response.status_code)


# swagger documentation and function to delete message in rooms
@swagger_auto_schema(
    methods=["delete"],
    request_body=DeleteMessageSerializer,
    responses={400: "Error: Bad Request"},
)
@api_view(["DELETE"])
@db_init_with_credentials
def delete_message(request, message_id):
    """
    This function deletes message in rooms using message id (message_id)
    """
    if request.method == "DELETE":
        message_id = request.GET.get("message_id")
    try:
        message = DB.read("dm_messages", {"_id": message_id})
        if message:
            response = DB.delete("dm_mesages", {"_id": message_id})
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response("message not found", status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)






@api_view(["DELETE"])
@db_init_with_credentials
def delete_bookmark(request, room_id):
    """
    Deletes a saved bookmark in a room
    """
    try:
        room = DB.read("dm_rooms", {"id": room_id})
        bookmarks = room["bookmarks"] or []
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
    if  bookmarks is not None:
        name = request.query_params.get("name", "")
        for bookmark in bookmarks:
            if name == bookmark.get("name", ""):
                bookmarks.remove(bookmark)
                break
        data = {"bookmarks": bookmarks}
        response = DB.update("dm_rooms", room_id, data=data)
        if response.get("status") == 200:
            return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)