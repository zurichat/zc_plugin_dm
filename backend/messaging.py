import json
from typing import Dict, List
import uuid
import re
from asgiref.sync import sync_to_async
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
    methods=["post", "get"],
    query_serializer=GetMessageSerializer,
    operation_summary="Creates and get messages",
    responses={201: MessageResponse, 400: "Error: Bad Request"},
)
@sync_to_async
@api_view(["GET", "POST"])
@db_init_with_credentials
def message_create_get(request, room_id):
    if request.method == "GET":
        paginator = PageNumberPagination()
        paginator.page_size = 20
        date = request.GET.get("date", None)
        params_serializer = GetMessageSerializer(data=request.GET.dict())
        if params_serializer.is_valid():
            room = DB.read_query("dm_rooms", query={"_id": room_id})
            if room:
                messages = get_room_messages(room_id, DB.organization_id)
                if date != None:
                    messages_by_date = get_messages(room_id, DB.organization_id, date)

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
            return Response(
                params_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    elif request.method == "POST":
        request.data["room_id"] = room_id
        serializer = MessageSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            room_id = data["room_id"]  # room id gotten from client request

            room = DB.read_query("dm_rooms", query={"_id": room_id})
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
        data = {
            "message_id": message_id,
            "pinned": pin,
            "Event": "unpin_message",
        }  # this event key is in capslock
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


@swagger_auto_schema(
    methods=["get"],
    operation_summary="Returns all messages in the dm collection",
    responses={200: "success", 424: "Failed Dependency"},
)
@api_view(["GET"])
@db_init_with_credentials
def all_messages(request):
    """This endpoint is used to get all the messages in the dm_messages collection.
    Also returns a messages with the read and unread status"""

    res = DB.read("dm_messages")
    if res and "status_code" not in res:
        all_messages = res
        read_messages = [
            message for message in all_messages if message["read"] == "true"
        ]
        unread_messages = [
            message for message in all_messages if message["read"] == "false"
        ]
        message_data = {
            "all_messages": all_messages,
            "read_messages": read_messages,
            "unread_messages": unread_messages,
        }
        return Response(message_data, status=status.HTTP_200_OK)

    else:
        return Response(
            f"something went wrong. message collection returned{res}",
            status=status.HTTP_424_FAILED_DEPENDENCY,
        )


class MessageDetailsView(APIView):
    def get(self, request, message_id, org_id):

        """
        Gets a single message from a room.
        It access room with the 'message_id' and then displays the message if it exists.
        The id of the organization (org_id) where the room is located is also needed.
        Parameters:
            org_id (str)        : This is the id of the organization th user belongs to.
            message_id (str)    : This is the unique id of the message to be deleted from a given room.

        Returns:
            A dict object indicating the the message has been deleted. Example:
            {
                "status"        : "success",
                "room_id"       : "6169dbcef5998a09e3bbbcd3",
                "message_id"    : "616ad4f989454c2006018af2"
                "message"       : "The message"
            }
        Raises:
            Not Found: If there is no message with specified id in the specified room, it returns 'message not found' and a '404' error message.
            IOError: An error occurred while deleteing the message.
        """
        data_storage = DataStorage()
        data_storage.organization_id = org_id
        data = request.data
        request.data["message_id"] = message_id

        try:
            message = data_storage.read("dm_messages", {"_id": message_id})

            room_id = message["room_id"]
            data = {
                "status": "success",
                "message": message,
            }
            return Response(data, status=status.HTTP_200_OK)

        except:

            return JsonResponse(
                {"message": "The room does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, message_id, org_id):
        """
        This is used to update message context using message id as identifier,

        Updates a message from a room.
        It access room with the 'room_id' and the message in the room with 'message_id' and then the new message.
        The id of the organization (org_id) where the room is located is also needed.
        Parameters:
            org_id (str)        : This is the id of the organization th user belongs to.
            message (str)       : This is the unique id of the message to be sent to a given room.
            room_id(str)        : This is the unique id of the room in the message

        Returns:
            A dict object indicating the the message has been updated. Example:
            {
                "status"        : "success",
                "room_id"       : "6169dbcef5998a09e3bbbcd3",
                "message_id"    : "616ad4f989454c2006018af2"
                "message"       : "The message"
            }
        Raises:
            Not Found: If there is no message with specified id in the specified room, it returns 'message not found' and a '404' error message.
            IOError: An error occurred while deleteing the message.
        """

        data_storage = DataStorage()
        data_storage.organization_id = org_id
        data = request.data
        data["message_id"] = message_id
        room_id = data["room_id"]
        message_get = data_storage.read("dm_messages", {"_id": message_id})

        # Checks DB for message using the message_id
        room_serializer = MessageSerializer(
            message_get, data=request.data, partial=True
        )

        # validates room_serializer with MessageSerializer.
        if room_serializer.is_valid():
            room_data = room_serializer.data
            new_data = {"message": data["message"]}
            response = DB.update(
                "dm_messages", message_id, new_data
            )  # moves on to update the mesage

            if response.get("status") == 200:
                data = {
                    "sender_id": request.data["sender_id"],
                    "message_id": message_id,
                    "room_id": room_id,
                    "message": new_data["message"],
                    "event": "edited_message",
                }
                centrifugo_data = send_centrifugo_data(room=room_id, data=data)

                if centrifugo_data.get("error", None) == None:
                    return Response(data=data, status=status.HTTP_201_CREATED)

                return Response(data)

        return Response(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, message_id, org_id):
        """
        Deletes a message from a room.

        It access room with the 'room_id' and the message in the room with 'message_id' and then deletes the message if it exists.
        The id of the organization (org_id) where the room is located is also needed.

        Parameters:
            org_id (str)        : This is the id of the organization th user belongs to.

            room_id (str)       : This is the unique id of the room the message to be deleted is in.

            message_id (str)    : This is the unique id of the message to be deleted from a given room.

        Returns:
            A dict object indicating the the message has been deleted. Example:
            {
                "status"        : "success",
                "event"         : "message_delete",
                "room_id"       : "6169dbcef5998a09e3bbbcd3",
                "message_id"    : "616ad4f989454c2006018af2"
            }

        Raises:
            Not Found: If there is no message with specified id in the specified room, it returns 'message not found' and a '404' error message.

            IOError: An error occurred while deleteing the message.
        """

        try:
            # Sends a get request to the database to fetch the message and the room of the message from.
            data_storage = DataStorage()
            data_storage.organization_id = org_id
            data = request.data
            data["message_id"] = message_id
            message = data_storage.read("dm_messages", {"_id": message_id})
            room_id = message["room_id"]

            # Checks if the room exists and if the message exists in the room.
            # If this returns true, the message is deleted. Else an error message is returned.
            if message:
                response = data_storage.delete("dm_messages", message_id)

                # if the delete operation was successful, it returns a success message.
                if response.get("status") == 200:
                    response_output = {
                        "status": response["message"],
                        "event": "message_delete",
                        "room_id": room_id,
                        "message_id": message_id,
                    }

                    # This publishes the operation across all active devices in the room where the operation was performed.
                    centrifugo_data = centrifugo_client.publish(
                        room=room_id, data=response
                    )

                    # Checks if the publish was successful and returns a success message if True, else an error message is returned.
                    if centrifugo_data.get("status_code") == 200:
                        return Response(response_output, status=status.HTTP_200_OK)

                    return Response(
                        data="message not sent",
                        status=status.HTTP_424_FAILED_DEPENDENCY,
                    )

            return Response("message not found", status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # All exeptions are caught are returned here...
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
