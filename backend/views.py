import uuid
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from .db import *

# Import Read Write function to Zuri Core
from .resmodels import *
from .serializers import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .centrifugo_handler import centrifugo_client


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
        },
        "success": "true",
    }

    return JsonResponse(info, safe=False)


def verify_user_auth(token):
    """
    Call Endpoint for verification of JWT Token
    Returns: py dict -> is_authenticated: boolean, & data: more info
    """
    url = "https://api.zuri.chat/auth/verify-token"

    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    api_response = requests.request("GET", url, headers=headers)

    json_response = api_response.json()

    response = {}
    if json_response["status"] == "200":
        response["is_authenticated"] = json_response["data"]["is_verified"]
        response["data"] = json_response["data"]["user"]
    else:
        response["is_authenticated"] = False
        response["data"] = json_response["message"]

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
    responses={201: MessageResponse, 400: "Error: Bad Request"},
)
@api_view(["POST"])
def send_message(request):
    """
    This endpoint is used to send message to user in rooms.
    It checks if room already exist before sending data.
    It makes a publish event to centrifugo after data
    is persisted
    """
    serializer = MessageSerializer(data=request.data)

    if serializer.is_valid():
        data = serializer.data
        room_id = data["room_id"]  # room id gotten from client request

        rooms = DB.read("dm_rooms")
        if type(rooms) == list:
            is_room_avalaible = (
                len([room for room in rooms if room.get("_id", None) == room_id]) != 0
            )

            if is_room_avalaible:
                response = DB.write("dm_messages", data=serializer.data)
                if response.get("status", None) == 200:

                    response_output = {
                        "status": response["message"],
                        "id": response["data"]["object_id"],
                        "room_id": room_id,
                        "thread": False,
                        "data": {
                            "sender_id": data["sender_id"],
                            "message": data["message"],
                            "created_at": data["created_at"],
                        },
                    }

                    centrifugo_data = send_centrifugo_data(
                        room=room_id, data=response_output
                    )  # publish data to centrifugo
                    if centrifugo_data["message"].get("error", None) == None:

                        return Response(
                            data=response_output, status=status.HTTP_201_CREATED
                        )

                return Response(
                    data="data not sent", status=status.HTTP_424_FAILED_DEPENDENCY
                )
            return Response("No such room", status=status.HTTP_400_BAD_REQUEST)
        return Response(
            "core server not avaliable", status=status.HTTP_424_FAILED_DEPENDENCY
        )

    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["post"],
    request_body=ThreadSerializer,
    responses={201: ThreadResponse, 400: "Error Response"},
)
@api_view(["POST"])
def send_thread_message(request):
    """
    This endpoint is used send messages as a thread
    under a message. It takes a message ID and
    validates if the message exists, then sends
    a publish event to centrifugo after
    thread message is persisted.
    """

    serializer = ThreadSerializer(data=request.data)

    if serializer.is_valid():
        data = serializer.data
        message_id = data["message_id"]
        messages = DB.read("dm_messages")  # fetch messages from zc core
        if type(messages) == list:
            message_list = [msg for msg in messages if msg["_id"] == message_id]

            if len(message_list) != 0:
                message = message_list[0]  # get messsage itself
                threads = message.get("threads", [])  # get threads

                del data["message_id"]  # remove message id from request to zc core
                data["_id"] = str(
                    uuid.uuid1()
                )  # assigns an id to each message in thread
                threads.append(data)  # append new message to list of thread

                response = DB.update(
                    "dm_messages", message["_id"], {"threads": threads}
                )  # update threads in db

                if response.get("status", None) == 200:

                    response_output = {
                        "status": response["message"],
                        "id": data["_id"],
                        "room_id": message["room_id"],
                        "message_id": message["_id"],
                        "thread": True,
                        "data": {
                            "sender_id": data["sender_id"],
                            "message": data["message"],
                            "created_at": data["created_at"],
                        },
                    }

                    centrifugo_data = send_centrifugo_data(
                        room=message["room_id"], data=response_output
                    )  # publish data to centrifugo
                    if centrifugo_data["message"].get("error", None) == None:
                        print("message is published to centrifugo")
                        return Response(
                            data=response_output, status=status.HTTP_201_CREATED
                        )
                return Response(
                    "data not sent", status=status.HTTP_424_FAILED_DEPENDENCY
                )
            return Response("No such message", status=status.HTTP_400_BAD_REQUEST)
        return Response(
            "core server not avaliable", status=status.HTTP_424_FAILED_DEPENDENCY
        )
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["post"],
    request_body=RoomSerializer,
    responses={201: CreateRoomResponse, 400: "Error: Bad Request"},
)
@api_view(["POST"])
def create_room(requests):
    """
    This function is used to create a room between 2 users.
    It takes the id of the users involved, sends a write request to the database .
    Then returns the room id when a room is successfully created
    """
    serializer = RoomSerializer(data=requests.data)

    if serializer.is_valid():
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
def getUserRooms(request):
    """
    This is used to retrieve all rooms a user is currently active in.
    It takes in a user_id as query param and returns the rooms for that user or a 204 status code
    if there is no room for the user_id or an invalid user_id.
    If the user_id is not provided, a 400 status code is returned.
    """
    if request.method == "GET":
        res = get_rooms(request.GET.get("user_id", None))
        query_param_serializer = UserRoomsSerializer(data=request.GET.dict())
        if query_param_serializer.is_valid():
            if len(res) == 0:
                return Response(
                    data="No rooms available", status=status.HTTP_204_NO_CONTENT
                )
            return Response(res, status=status.HTTP_200_OK)
        return Response(data="Provide a user_id", status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["get"],
    query_serializer=GetMessageSerializer,
    responses={201: MessageResponse, 400: "Error: Bad Request"},
)
@api_view(["GET"])
def getRoomMessages(request):
    """
    This is used to retrieve messages in a room. It takes a room_id and/or a date as query params.
    If only the room_id is provided, it returns a list of all the messages if available,
    or a 204 status code if there is no message in the room.
    If both room_id and date are provided, it returns all the messages in that room for that
    particular date.
    If there is no room_id in the query params, it returns a 404 status code.
    """
    if request.method == "GET":
        room_id = request.GET.get("room_id", None)
        date = request.GET.get("date", None)
        params_serializer = GetMessageSerializer(data=request.GET.dict())
        all_rooms = DB.read("dm_rooms")

        if params_serializer.is_valid():
            is_room_avalaible = (
                len([room for room in all_rooms if room.get("_id", None) == room_id])
                != 0
            )
            if is_room_avalaible:
                messages = get_room_messages(room_id)
                param_len = len(params_serializer.data)
                if param_len == 2:
                    messages_by_date = get_messages(messages, date)
                    if len(messages_by_date) == 0:
                        return Response(
                            data="No messages available",
                            status=status.HTTP_204_NO_CONTENT,
                        )
                    return Response(messages_by_date, status=status.HTTP_200_OK)
                else:
                    if len(messages) == 0:
                        return Response(
                            data="No messages available",
                            status=status.HTTP_204_NO_CONTENT,
                        )
                    return Response(messages, status=status.HTTP_200_OK)
            return Response(data="No such room", status=status.HTTP_400_BAD_REQUEST)
        return Response(
            data="Provide the room_id or/and date", status=status.HTTP_400_BAD_REQUEST
        )
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["get"],
    query_serializer=RoomInfoSerializer,
    responses={201: RoomInfoResponse, 400: "Error: Bad Request"},
)
@api_view(["GET"])
def room_info(request):
    """
    This is used to retrieve information about a room.
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
                    org_id = "6133c5a68006324323416896"
                room_data = {
                    "room_id": room_id,
                    "org_id": org_id,
                    "room_user_ids": room_user_ids,
                    "created_at": created_at,
                    "description": f"This room contains the coversation between {room_user_ids[0]} and {room_user_ids[1]}",
                }
                return Response(data=room_data, status=status.HTTP_200_OK)
        return Response(data="No such Room", status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# /code for updating room


@api_view(["GET", "POST"])
def edit_room(request, pk):
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
        room_serializer = MessageSerializer(message, data=request.data, partial=True)
        if room_serializer.is_valid():
            room_serializer.save()
            data = room_serializer.data
            # print(data)
            response = DB.update("dm_messages", pk, data)
            return Response(room_serializer.data)
        return Response(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(data="No Rooms", status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["get"], responses={201: MessageLinkResponse, 400: "Error: Bad Request"}
)
@api_view(["GET"])
def copy_message_link(request, message_id):
    """
    This is used to retrieve a single message. It takes a message_id as query params.
    If message_id is provided, it returns a dictionary with information about the message,
    or a 204 status code if there is no message with the same message id.
    I will use the message information returned to generate a link which contains a room_id and a message_id
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
def read_message_link(request, room_id, message_id):
    """
    This is used to retrieve a single message. It takes a message_id as query params.
    If message_id is provided, it returns a dictionary with information about the message,
    or a 204 status code if there is no message with the same message id.
    I will use the message information returned to generate a link which contains a room_id and a message_id
    """

    if request.method == "GET":
        message = DB.read("dm_messages", {"id": message_id, "room_id": room_id})
        return Response(data=message, status=status.HTTP_200_OK)
    else:
        return JsonResponse(
            {"message": "The message does not exist"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
def organization_members(request):
    """
    This endpoint returns a list of members for an organization.
    :returns: json response -> a list of objects (members) or 401_Unauthorized messages.
    """
    url = f"https://api.zuri.chat/organizations/{ORG_ID}/members"

    response = requests.get(url)

    if response.status_code == 200:
        response = response.json()["data"]
        return Response(response, status=status.HTTP_200_OK)
    return Response(response.json(), status=status.HTTP_401_UNAUTHORIZED)
