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


class ThreadListView(generics.ListCreateAPIView):
    """
    List all messages in thread, or create a new Thread message.
    """

    serializer_class = ThreadSerializer

    @swagger_auto_schema(
        operation_summary="Retrieves thread messages for a specific message",
        responses={
            200: "OK: Success!",
            400: "Error: Bad Request",
        },
    )
    # @method_decorator(db_init_with_credentials)
    def get(
        self,
        request,
        org_id: str,
        room_id: str,
        message_id: str,
    ) -> Response:
        """Retrieves all thread messages attached to a specific message

        Args:
            org_id (str): The organisation id
            room_id (str): The room id where the dm occured
            message_id (str): The message id for which we want to get the thread messages

        Returns:
            Response: Contains a list of thread messsages
        """
        # fetch message parent of the thread
        data_storage = DataStorage()
        data_storage.organization_id = org_id
        message = data_storage.read("dm_messages", {"_id": message_id, "room_id": room_id})
        paginator = PageNumberPagination()
        paginator.page_size = 20
        if message and message.get("status_code", None) == None:
            threads = message.get("threads")
            threads.reverse()
            response = paginator.paginate_queryset(threads, request)
            return paginator.get_paginated_response(response)       
        return Response("No such message", status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Create a thread message for a specific message",
        request_body=ThreadSerializer,
        responses={
            200: "OK: Success!",
            400: "Error: Bad Request",
        },
    )
    def post(
        self,
        request,
        org_id: str,
        room_id: str,
        message_id: str,
    ) -> Response:
        """
        Validates if the message exists, then sends
        a publish event to centrifugo after
        thread message is persisted.
        """

        data_storage = DataStorage()
        data_storage.organization_id = org_id
        request.data["message_id"] = message_id
        serializer = ThreadSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            message_id = data["message_id"]
            sender_id = data["sender_id"]

            message = data_storage.read(
                MESSAGES, {"_id": message_id, "room_id": room_id}
            )  # fetch message from zc

            if message and message.get("status_code", None) == None:
                threads = message.get("threads", [])  # get threads
                # remove message id from request to zc core
                del data["message_id"]
                # assigns an id to each message in thread
                data["_id"] = str(uuid.uuid1())
                threads.append(data)  # append new message to list of thread

                room = data_storage.read(ROOMS, {"_id": message["room_id"]})
                if sender_id in room.get("room_user_ids", []):

                    response = data_storage.update(
                        MESSAGES, message["_id"], {"threads": threads}
                    )  # update threads in db
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
                        "data not sent", status=status.HTTP_424_FAILED_DEPENDENCY
                    )
                return Response("sender not in room", status=status.HTTP_404_NOT_FOUND)
            return Response(
                "message or room not found", status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ThreadDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a single thread message, update a thread message or delete.
    """

    serializer_class = ThreadSerializer
    queryset = ""
    lookup_field = "thread_message_id"


    @swagger_auto_schema(
        operation_summary="Deletes a specifc thread message for a specific parent message",
        responses={
            200: "OK: Success!",
            400: "Error: Bad Request",
        },
    )
    def delete(
        self,
        request,
        org_id: str,
        room_id: str,
        message_id: str,
        thread_message_id: str,
    ) -> Response:
        """Deletes a specifc thread message for a specific parent message

        Args:
            request (Request): The incoming HTTP request
            org_id (str): The organisation id
            room_id (str): The room id where the dm occured
            message_id (str): The message id for which we want to get the thread messages
            thread_message_id (str): The thread message id to delete

        Returns:
            Response: Contains a new list of thread messsages
        """
        data_storage = DataStorage()
        data_storage.organization_id = org_id
        message = data_storage.read(MESSAGES, {"_id": message_id, "room_id": room_id})
        if message and message.get("status_code", None) == None:
            threads: List[Dict] = message.get("threads")
            if threads:
                for thread in threads:
                    # removes the specific thread message
                    if thread_message_id == thread.get("_id"):
                        threads.remove(thread)
                        break
                data = {"threads": threads}
                response = data_storage.update(MESSAGES, message_id, data=data)
                if response.get("status", None) == 200:
                    response_output = {
                        "status": response["message"],
                        "event": "thread_message_delete",
                        "thread_id": thread_message_id,
                        "room_id": room_id,
                        "message_id": message_id,
                        "data": {
                            "threads": threads,
                        },
                    }
                    try:
                        # publish data to centrifugo
                        centrifugo_data = centrifugo_client.publish(
                            room=room_id, data=response_output
                        )
                        if (
                            centrifugo_data
                            and centrifugo_data.get("status_code") == 200
                        ):
                            return Response(
                                data=response_output, status=status.HTTP_200_OK
                            )
                        else:
                            return Response(
                                data="Message not sent",
                                status=status.HTTP_424_FAILED_DEPENDENCY,
                            )
                    except:
                        return Response(
                            data="Centrifugo server not available",
                            status=status.HTTP_424_FAILED_DEPENDENCY,
                        )

        return Response(status=status.HTTP_400_BAD_REQUEST)


    def put(
        self,
        request,
        org_id: str,
        room_id: str,
        message_id: str,
        thread_message_id: str):

        data_storage = DataStorage()
        data_storage.organization_id = org_id
        thread_serializer = ThreadSerializer(data=request.data)
        if thread_serializer.is_valid():
            thread_data = thread_serializer.data
            sender_id = thread_data["sender_id"]
            message_id = thread_data["message_id"]
            messages = data_storage.read("dm_messages", {"room_id": room_id})
            if messages:
                if "status_code" in messages:
                    if messages.get("status_code") == 404:
                        return Response(
                            data="No data on zc core", status=status.HTTP_404_NOT_FOUND
                        )
                    return Response(
                        data="Problem with zc core",
                        status=status.HTTP_424_FAILED_DEPENDENCY,
                    )
                for message in messages:
                    if message.get("_id") == message_id:
                        thread = message
                        break
                    thread = None
                if thread:
                    thread_messages = thread.get("threads", [])
                    for thread_message in thread_messages:
                        if thread_message.get("_id") == thread_message_id:
                            current_thread_message = thread_message
                            break
                        current_thread_message = None
                    if current_thread_message:
                        if (
                            current_thread_message["sender_id"] == sender_id
                            and thread["_id"] == message_id
                        ):
                            current_thread_message["message"] = thread_data["message"]
                            response = data_storage.update(
                                "dm_messages",
                                thread["_id"],
                                {"threads": thread_messages},
                            )
                            if response and response.get("status") == 200:
                                response_output = {
                                    "status": response["message"],
                                    "event": "thread_message_update",
                                    "thread_id": current_thread_message["_id"],
                                    "room_id": thread["room_id"],
                                    "message_id": thread["_id"],
                                    "thread": True,
                                    "data": {
                                        "sender_id": thread_data["sender_id"],
                                        "message": thread_data["message"],
                                        "created_at": thread_data["created_at"],
                                    },
                                    "edited": True,
                                }
                                try:
                                    centrifugo_data = centrifugo_client.publish(
                                        room=room_id, data=response_output
                                    )
                                    if (
                                        centrifugo_data
                                        and centrifugo_data.get("status_code") == 200
                                    ):
                                        return Response(
                                            data=response_output,
                                            status=status.HTTP_201_CREATED,
                                        )
                                    else:
                                        return Response(
                                            data="Message not sent",
                                            status=status.HTTP_424_FAILED_DEPENDENCY,
                                        )
                                except Exception:
                                    return Response(
                                        data="Centrifugo server not available",
                                        status=status.HTTP_424_FAILED_DEPENDENCY,
                                    )
                            return Response(
                                data="Message not updated",
                                status=status.HTTP_424_FAILED_DEPENDENCY,
                            )
                        return Response(
                            data="Sender_id or message_id invalid",
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                    return Response(
                        data="Thread message not found",
                        status=status.HTTP_404_NOT_FOUND,
                    )
                return Response(
                    data="Message not found", status=status.HTTP_404_NOT_FOUND
                )
            return Response(data="Room not found", status=status.HTTP_404_NOT_FOUND)
        return Response(thread_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["PUT"])
@db_init_with_credentials
def update_thread_read_status(request, room_id, message_id, thread_message_id):
    message = DB.read("dm_messages", {"_id": message_id, "room_id": room_id})
    if message:
        if "status_code" in message:
            if "status_code" == 404:
                return Response(
                    data="No data on zc core", 
                    status=status.HTTP_404_NOT_FOUND
                    )
            return Response(
                data="Problem with zc core", 
                status=status.HTTP_424_FAILED_DEPENDENCY
                )
        else:
            thread_message = [thread for thread in message["threads"] if thread["_id"] == thread_message_id]
            if thread_message:
                thread_message[0]["read"] = not thread_message[0]["read"]
                data = {"read": thread_message[0]["read"]}
                response = DB.update("dm_messages", message_id, {"threads": message["threads"]})
                if response and response.get("status") == 200:
                    return Response(
                        data, 
                        status=status.HTTP_201_CREATED
                        )
                return Response(
                    data="Message status not updated", 
                    status=status.HTTP_424_FAILED_DEPENDENCY
                    )
            return Response(
                data="Thread message not found", 
                status=status.HTTP_404_NOT_FOUND
                )
    return Response(
        data="Parent message not found", 
        status=status.HTTP_404_NOT_FOUND
        )


@api_view(["POST"])
@db_init_with_credentials
def send_thread_message_to_channel(request, room_id, message_id, thread_message_id):
    parent_message = DB.read("dm_messages", {"_id": message_id, "room_id": room_id})
    if parent_message:
        if "status_code" in parent_message:
            if "status_code" == 404:
                return Response(
                    data="No data on zc core", 
                    status=status.HTTP_404_NOT_FOUND
                    )
            return Response(
                data="Problem with zc core", 
                status=status.HTTP_424_FAILED_DEPENDENCY
                )
        thread_message = [thread for thread in parent_message["threads"] if thread["_id"] == thread_message_id]
        if thread_message:
            sender_id = thread_message[0]["sender_id"]
            message = thread_message[0]["message"]
            url = f"https://dm.zuri.chat/api/v1/org/{DB.organization_id}/rooms/{room_id}/messages"
            payload = json.dumps(
                {
                "sender_id": f"{sender_id}",
                "room_id": f"{room_id}",
                "message": f"{message}",
                }
            )
            headers = {"Content-Type": "application/json"}
            send_message = requests.request("POST", url, headers=headers, data=payload)
            if send_message.status_code == 201:
                return Response(
                    send_message.json(), 
                    status=status.HTTP_201_CREATED
                    )
            return Response(
                send_message.json(), 
                status=response.status_code
                )
        return Response(
            data="No thread message found", 
            status=status.HTTP_404_NOT_FOUND
            )
    return Response(
        data="No message or room found", 
        status=status.HTTP_404_NOT_FOUND
        )

@api_view(["GET"])
@db_init_with_credentials
def copy_thread_message_link(request, room_id, message_id, thread_message_id):
    """
    Retrieves a single thread message using the thread_message_id as query params.
    The message information returned is used to generate a link which contains 
    a room_id, parent_message_id and a thread_message_id
    """
    parent_message = DB.read("dm_messages", {"id": message_id, "room_id": room_id})
    if parent_message:
        if "status_code" in parent_message:
            if "status_code" == 404:
                return Response(
                    data="No data on zc core", 
                    status=status.HTTP_404_NOT_FOUND
                    )
            return Response(
                data="Problem with zc core", 
                status=status.HTTP_424_FAILED_DEPENDENCY
                )
        thread_message = [thread for thread in parent_message["threads"] if thread["_id"] == thread_message_id]
        if thread_message:
            message_info = {
                "room_id": room_id,
                "parent_message_id": message_id,
                "thread_id": thread_message_id,
                "link": f"https://dm.zuri.chat/thread_message/{DB.organization_id}/{room_id}/{message_id}/{thread_message_id}",
            }
            return Response(
                data=message_info, 
                status=status.HTTP_200_OK
                )
        return Response(
            data="No such thread message", 
            status=status.HTTP_404_NOT_FOUND
            )
    return Response(
        data="No parent message found", 
        status=status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
@db_init_with_credentials
def read_thread_message_link(request, room_id, message_id, thread_message_id):
    message = DB.read("dm_messages", {"id": message_id, "room_id": room_id})
    if message:
        if "status_code" in message:
            if "status_code" == 404:
                return Response(
                    data="No data on zc core", 
                    status=status.HTTP_404_NOT_FOUND
                    )
            return Response(
                data="Problem with zc core", 
                status=status.HTTP_424_FAILED_DEPENDENCY
                )
        thread_message = [thread for thread in message["threads"] if thread["_id"] == thread_message_id]
        if thread_message:
            return JsonResponse({"message": thread_message[0]["message"]})
        return Response(
            data="No such thread message", 
            status=status.HTTP_404_NOT_FOUND
            )
    return Response(
        data="Parent message not found", 
        status=status.HTTP_404_NOT_FOUND
        )


@api_view(["PUT"])
@db_init_with_credentials
def pinned_thread_message(request, room_id, message_id, thread_message_id):
    message = DB.read("dm_messages", {"id": message_id, "room_id": room_id})
    if message:
        if "status_code" in message:
            if "status_code" == 404:
                return Response(
                    data="No data on zc core", 
                    status=status.HTTP_404_NOT_FOUND
                    )
            return Response(
                data="Problem with zc core", 
                status=status.HTTP_424_FAILED_DEPENDENCY
                )
        room = DB.read("dm_rooms", {"id": room_id})
        pin = room["pinned"] or []
        thread_message = [thread for thread in message["threads"] if thread["_id"] == thread_message_id]
        if thread_message:
            pinned_thread_list = [thread_pin for thread_pin in pin if isinstance(thread_pin, dict)]
            pinned_thread_ids = [val.get("thread_message_id") for val in pinned_thread_list]
            if thread_message_id in pinned_thread_ids:
                current_pin = {key:value for (key,value) in pinned_thread_list.items() if value == thread_message_id}
                pin.remove(current_pin)
                data = {
                    "message_id": message_id, 
                    "thread_id": thread_message_id, 
                    "pinned": pin, 
                    "Event": "unpin_thread_message"
                }
                response = DB.update("dm_rooms", room_id, {"pinned": pin})
                if response["status"] == 200:
                    centrifugo_data = send_centrifugo_data(
                        room=room_id, data=data
                    )  # publish data to centrifugo
                    if centrifugo_data.get("error", None) == None:
                        return Response(
                            data=data, status=status.HTTP_201_CREATED
                            )
                else:
                    return Response(
                        status=response.status_code
                        )
            else:
                current_pin = {
                    "message_id": message_id, 
                    "thread_message_id": thread_message_id
                }
                pin.append(current_pin)
                data = {
                    "message_id": message_id, 
                    "thread_id": thread_message_id, 
                    "pinned": pin, 
                    "Event": "pin_thread_message"
                }
                response = DB.update("dm_rooms", room_id, {"pinned": pin})
                centrifugo_data = send_centrifugo_data(
                    room=room_id, data=data
                )  # publish data to centrifugo
                if centrifugo_data.get("error", None) == None:
                    return Response(
                        data=data, 
                        status=status.HTTP_201_CREATED
                        )
        return Response(
            data="No such thread message", 
            status=status.HTTP_404_NOT_FOUND
            )
    return Response(
        data="Parent message not found", 
        status=status.HTTP_404_NOT_FOUND
        )



@api_view(["GET"])
@db_init_with_credentials
def get_all_threads(request, member_id: str):
    threads_list = LifoQueue()
    # org_id = request.GET.get("")

    if request.method == "GET":
        rooms = get_rooms(user_id=member_id, org_id=DB.organization_id)
        if rooms:
            # print(f"the room ", rooms)
            for room in rooms:
                # print(f"the room ", room)
                data = {}
                data["room_id"] = room.get("_id")
                data["room_name"] = room.get("room_name")
                messages = DB.read(MESSAGES, {"room_id": room.get("_id")})
                if messages:
                    if messages.get("status_code") == 404:
                        return Response(
                            data="No message in this room",
                            status=status.HTTP_404_NOT_FOUND,
                        )
                    # print(f"mrssages ", messages)
                    for message in messages:
                        threads = message.get("threads")
                        if threads:
                            print(threads)
                        return Response(
                            data="No threads found", status=status.HTTP_204_NO_CONTENT
                        )
                threads_list.put(data)
                print(f"lst qur", threads_list)
                return Response(
                    data="No messages found", status=status.HTTP_204_NO_CONTENT
                )

        return Response(data="No rooms created yet", status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_400_BAD_REQUEST)
