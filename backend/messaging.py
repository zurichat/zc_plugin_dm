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
    methods=["post","get"],
    query_serializer=GetMessageSerializer,
    operation_summary="Creates and get messages",
   responses={
            201: MessageResponse,
            400: "Error: Bad Request"
        }
)
@api_view(["GET","POST"])
@db_init_with_credentials
def message_create_get(request, room_id):
    if request.method == "GET":
        paginator = PageNumberPagination()
        paginator.page_size = 20
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
                    else:
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
                    result_page = paginator.paginate_queryset(messages, request)
                    return paginator.get_paginated_response(result_page)
            else:
                return Response(data="No such room", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(params_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "POST":
        request.data["room_id"] = room_id
        print(request)
        serializer = MessageSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            room_id = data["room_id"]  # room id gotten from client request

            room = DB.read("dm_rooms", {"_id": room_id})
            if room and room.get("status_code", None) == None:
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



@api_view(["GET", "PUT"])
@db_init_with_credentials
def edit_message(request, message_id, room_id):
    """
    This is used to update message context using message id as identifier,
    first --> we check if this message exist, if it does not exist we raise message doesnot exist,
    if above message exists:
        pass GET request to view the message one whats to edit.
        or pass POST with data to update


    """
    if request.method == "GET":
        try:
            message = DB.read("dm_messages", {"id": message_id})
            print(message)
            return Response(message)
        except:
            return JsonResponse(
                {"message": "The room does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

    else:
        message = DB.read("dm_messages", {"id": message_id})
        room_serializer = MessageSerializer(message, data=request.data, partial=True)
        if room_serializer.is_valid():
            data = room_serializer.data
            data = {"message":request.data["message"]}
            # print(data)
            response = DB.update("dm_messages", message_id, data)
            if response.get("status") == 200:
                data = {
                        "sender_id":request.data["sender_id"],
                        "message_id":message_id,
                        "room_id":room_id,
                        "message":request.data["message"],
                        "event":"edited_message"
                        }
                centrifugo_data = send_centrifugo_data(
                    room=room_id, data=data
                )
                if centrifugo_data.get("error", None) == None:
                    return Response(data=data, status=status.HTTP_201_CREATED)
                return Response(data)
        return Response(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["delete"],
    operation_summary="Deletes messages from rooms",
    request_body=DeleteMessageSerializer,
    responses={400: "Error: Bad Request"},
)
@api_view(["DELETE"])
@db_init_with_credentials
def delete_message(request, message_id, room_id):
    """
    This function deletes message in rooms using message
    organization id (org_id), room id (room_id) and the message id (message_id).
    """
    message_id = request.GET.get("message_id")
    room_id = request.GET.get("room_id")
    if request.method == "DELETE":
        try:
            message = DB.read("dm_messages", {"_id": message_id})
            room = DB.read("dm_rooms", {"_id": room_id})

            if room and message:
                response = DB.delete("dm_messages", {"_id": message_id})
                centrifugo_data = centrifugo_client.publish(
                    message=message_id, data=response
                )
                if centrifugo_data and centrifugo_data.status_code == 200:
                    return Response(response, status=status.HTTP_200_OK)
            return Response("message not found", status=status.HTTP_404_NOT_FOUND)
        except exception_handler as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(
    methods=["post"],
    operation_summary="Schedules messages in rooms",
    request_body=ScheduleMessageSerializer,
    responses={
        201: "Success: Message Scheduled",
        400: "Error: Bad Request",
    },
)
@api_view(["POST"])
@db_init_with_credentials
def scheduled_messages(request, room_id):
    ORG_ID = DB.organization_id

    schedule_serializer = ScheduleMessageSerializer(data=request.data)
    if schedule_serializer.is_valid():
        data = schedule_serializer.data

        sender_id = data["sender_id"]
        room_id = data["room_id"]
        message = data["message"]
        timer = data["timer"]

        now = datetime.now()
        timer = datetime.strptime(timer, "%Y-%m-%d %H:%M:%S")
        duration = timer - now
        duration = duration.total_seconds()

        url = f"https://dm.zuri.chat/api/v1/org/{ORG_ID}/rooms/{room_id}/messages"
        payload = json.dumps(
            {
                "sender_id": f"{sender_id}",
                "room_id": f"{room_id}",
                "message": f"{message}",
            }
        )
        headers = {"Content-Type": "application/json"}
        time.sleep(duration)
        response = requests.request("POST", url, headers=headers, data=payload)
    else:
        return Response(schedule_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if response.status_code == 201:
        return Response(response.json(), status=status.HTTP_201_CREATED)
    return Response(response.json(), status=response.status_code)



@swagger_auto_schema(
    methods=["put"],
    operation_summary="Marks a message as read or unread",
    responses={
        200: "Ok: Success",
        400: "Error: Bad Request",
        503: "Server Error: Service Unavailable",
    },
)
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
    operation_summary="Pins a message in a room",
    responses={
        200: PinMessageResponse,
        400: "Error: Bad Request",
        503: "Server Error: Service Unavailable",
    },
)
@api_view(["PUT"])
@db_init_with_credentials
def pinned_message(request, message_id):
    """
    This is used to pin a message.
    The message_id is passed to it which
    reads through the database, gets the room id,
    generates a link and then add it to the pinned key value.

    If the link already exist, it will unpin that particular message already pinned.
    """
    try:
        message = DB.read("dm_messages", {"id": message_id})
        if message:
            room_id = message["room_id"]
            room = DB.read("dm_rooms", {"id": room_id})
            pin = room["pinned"] or []
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
    if message_id in pin:
        pin.remove(message_id)
        data = {"message_id": message_id, "pinned": pin, "Event": "unpin_message"} # this event key is in capslock
        response = DB.update("dm_rooms", room_id, {"pinned": pin})
        # room = DB.read("dm_rooms", {"id": room_id})
        if response["status"] == 200:
            centrifugo_data = send_centrifugo_data(
                room=room_id, data=data
            )  # publish data to centrifugo
            if centrifugo_data.get("error", None) == None:
                return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=response.status_code)
    else:
        pin.append(message_id)
        data = {"message_id": message_id, "pinned": pin, "Event": "pin_message"}
        response = DB.update("dm_rooms", room_id, {"pinned": pin})
        # room = DB.read("dm_rooms", {"id": room_id})
        centrifugo_data = send_centrifugo_data(
            room=room_id, data=data
        )  # publish data to centrifugo
        if centrifugo_data.get("error", None) == None:
            return Response(data=data, status=status.HTTP_201_CREATED)
