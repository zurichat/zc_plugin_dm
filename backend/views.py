from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from .db import *
from rest_framework.views import (
    APIView,
    exception_handler,
)
# Import Read Write function to Zuri Core
from .resmodels import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from datetime import datetime
from .centrifugo_handler import centrifugo_client
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
            "homepage_url": "https://dm.zuri.chat/dm",
            "create_room_url": "https://dm.zuri.chat/api/v1/<str:org_id>/room",
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
    user_id = request.GET.get("user", None)
    user_rooms = get_rooms(user_id, org_id)
    rooms = []
    if user_rooms != None:
        for room in user_rooms:
            if "org_id" in room:
                if org_id == room["org_id"]:
                    room_profile = {}
                    room_profile["room_id"] = room["_id"]
                    room_profile["room_url"] = f"/dm/{org_id}/{room['_id']}/{user_id}"
                    for id in room["room_user_ids"]:
                        if id != user_id:
                            profile = get_user_profile(org_id, id)
                            if profile["status"] == 200:
                                room_profile["room_name"] = profile["data"]["user_name"]
                                if profile["data"]["image_url"]:
                                    room_profile["room_image"] = profile["data"]["image_url"]
                                else:
                                    room_profile["room_image"] = "https://cdn.iconscout.com/icon/free/png-256/account-avatar-profile-human-man-user-30448.png"
                    rooms.append(room_profile)
                    
    side_bar = {
        "name": "DM Plugin",
        "description": "Sends messages between users",
        "plugin_id": "6135f65de2358b02686503a7",
        "organisation_id": f"{org_id}",
        "user_id": f"{user_id}",
        "group_name": "DM",
        "category":"direct messages",
        "show_group": False,
        "button_url":f"/dm/{org_id}/{user_id}/all-dms",
        "public_rooms": [],
        "joined_rooms": rooms,
        # List of rooms/collections created whenever a user starts a DM chat with another user
        # This is what will be displayed by Zuri Main
    }
    return JsonResponse(side_bar, safe=False)

@swagger_auto_schema(
    methods=["get"],
    operation_summary="Retreives messages in a room using a filter",
    responses={
        200: FilterMessageResponse,
        204: "Ok: No messages available",
        400: "Error: No such room or invalid Room",
    },
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



@swagger_auto_schema(
    methods=["post"],
    operation_summary="Creates message reminders in rooms",
    request_body=ReminderSerializer,
    responses={400: "Error: Bad Request"},
)
@api_view(["POST"])
@db_init_with_credentials
def create_reminder(request):
    """
        This is used to remind a user about a  message
        Your body request should have the format
        {
        "message_id": "6146ea68845b436ea04d107d",
        "current_date": "Tue, 22 Nov 2011 06:00:00 GMT",
        "scheduled_date":"Tue, 22 Nov 2011 06:10:00 GMT",
        "notes": "fff"
    }
    """
    serializer = ReminderSerializer(data=request.data)
    if serializer.is_valid():
        serialized_data = serializer.data
        message_id = serialized_data['message_id']
        current_date = serialized_data['current_date']
        scheduled_date = serialized_data['scheduled_date']
        try:
            notes_data = serialized_data['notes']
        except:
            notes_data = ""
        ##calculate duration and send notification
        local_scheduled_date = datetime.strptime(scheduled_date,'%a, %d %b %Y %H:%M:%S %Z')
        utc_scheduled_date = local_scheduled_date.replace(tzinfo=timezone.utc)

        local_current_date = datetime.strptime(current_date, "%a, %d %b %Y %H:%M:%S %Z")
        utc_current_date = local_current_date.replace(tzinfo=timezone.utc)
        duration = local_scheduled_date - local_current_date
        duration_sec = duration.total_seconds()
        if duration_sec > 0:
            # get message infos , sender info and recpient info
            message = DB.read("dm_messages", {"id": message_id})
            if message:
                room_id = message["room_id"]
                try:
                    room = DB.read("dm_rooms", {"_id": room_id})
  
                except Exception as e:
                    print(e)
                    return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE) 
                users_in_a_room = room.get("room_user_ids",[]).copy()
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
                    "scheduled_date": scheduled_date,
                }
                if len(notes_data) > 0:
                    try:
                        notes = message["notes"] or []
                        notes.append(notes_data)
                        response = DB.update(
                            "dm_messages", message_id, {"notes": notes}
                        )
                    except Exception as e:
                        notes = []
                        notes.append(notes_data)
                        response = DB.update(
                            "dm_messages", message_id, {"notes": notes}
                        )
                    if response.get("status") == 200:
                        response_output["notes"] = notes
                        return Response(data = response_output,status=status.HTTP_201_CREATED)
                # SendNotificationThread(duration,duration_sec,utc_scheduled_date, utc_current_date).start()
                return Response(data=response_output, status=status.HTTP_201_CREATED)
            return Response(data="No such message", status=status.HTTP_400_BAD_REQUEST)
        return Response(
            data="Your current date is ahead of the scheduled time. Are you plannig to go back in time?",
            status=status.HTTP_400_BAD_REQUEST,
        )
    return Response(data="Bad Format ", status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def PING(request):
    url = "https://api.zuri.chat"
    try:
        response = requests.get(url, headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            server = {"server": True}
            return Response(data=server)
    except Exception:
        print("Either problem occured in the database or the url you entered is wrong")
        print("Please check url and try again or")
        print("Please wait for some time and try again")
        server = {
            "server": False,
        }
        return Response(data=server)
    except:
        server = {"server": False}
        return JsonResponse(data=server)




@api_view(["POST"])
@db_init_with_credentials
def send_reply(request, room_id, message_id):
    """
    This endpoint is used to send a reply message
    It takes in the a room_id and the message_id of the message being replied to
    Stores the data of the replied message in a field "replied message"
    """
    request.data["room_id"] = room_id
    print(request)
    serializer = MessageSerializer(data=request.data)
    reply_response = DB.read("dm_messages", {"_id": message_id})
    if reply_response and reply_response.get("status_code", None) == None:
        replied_message = reply_response
    else:
        return Response("Message being replied to doesn't exist, FE pass in correct message id", status=status.HTTP_400_BAD_REQUEST)
    print(reply_response)

    if serializer.is_valid():
        data = serializer.data
        room_id = data["room_id"]  # room id gotten from client request

        room = DB.read("dm_rooms", {"_id": room_id})
        if room and room.get("status_code", None) == None:
            if data["sender_id"] in room.get("room_user_ids", []):
                data["replied_message"] = replied_message
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
                            "replied_message": data["replied_message"]
                        },
                    }
                    try:
                        centrifugo_data = centrifugo_client.publish(
                            room=room_id, data=response_output
                        )  # publish data to centrifugo
                        if (
                            centrifugo_data
                            and centrifugo_data.get("status_code") == 200
                        ):
                            return Response(
                                data=response_output, status=status.HTTP_201_CREATED
                            )
                        else:
                            return Response(
                                data="message not sent",
                                status=status.HTTP_424_FAILED_DEPENDENCY,
                            )
                    except:
                        return Response(
                            data="centrifugo server not available",
                            status=status.HTTP_424_FAILED_DEPENDENCY,
                        )
                return Response(
                    data="message not saved and not sent",
                    status=status.HTTP_424_FAILED_DEPENDENCY,
                )
            return Response(
                "sender not in room", status=status.HTTP_400_BAD_REQUEST
            )
        return Response("room not found", status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def test_search(request):

    return render(request, 'test.html')