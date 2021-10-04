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



class Emoji(APIView):
    """
    List all Emoji reactions, or create a new Emoji reaction.
    """

    @swagger_auto_schema(
        operation_summary="Retrieves reactions to messages",
        responses={
            200: "OK: Success!",
            400: "Error: Bad Request",
        },
    )
    # @method_decorator(db_init_with_credentials)
    def get(self, request, org_id: str, room_id: str, message_id: str):
        # fetch message related to that reaction
        message = DB.read("dm_messages", {"_id": message_id, "room_id": room_id})
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
        operation_summary="Creates and keeps tracks of reactions to messages",
        responses={201: "OK: Success!", 400: "Error: Bad Request"},
    )
    # @method_decorator(db_init_with_credentials)
    def post(self, request, org_id: str, room_id: str, message_id: str):
        request.data["message_id"] = message_id
        serializer = EmojiSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            data["count"] += 1
            message_id = data["message_id"]
            sender_id = data["sender_id"]

            # fetch message related to that reaction
            message = DB.read("dm_messages", {"_id": message_id, "room_id": room_id})
            if message:
                # get reactions
                reactions = message.get("reactions", [])
                reactions.append(data)

                room = DB.read(ROOMS, {"_id": message["room_id"]})
                if room:
                    # update reactions for a message
                    response = DB.update(MESSAGES, message_id, {"reactions": reactions})
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
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )



class ThreadEmoji(APIView):
    """
    List all Emoji reactions, or create a new Emoji reaction.
    """
    def get(
        self,
        request,
        org_id: str,
        room_id: str,
        message_id: str,
        thread_message_id: str):

        data_storage = DataStorage()
        data_storage.organization_id = org_id
        message = data_storage.read("dm_messages", {"_id": message_id, "room_id": room_id})
        if message:
            if "status_code" in message:
                return Response(
                    data="Unable to retrieve data from zc core",
                    status=status.HTTP_424_FAILED_DEPENDENCY
                    )
            current_thread_message = [thread for thread in message["threads"] if thread["_id"] == thread_message_id]
            if current_thread_message:
                return Response(
                    data={
                        "status": "200",
                        "event": "get_thread_message_reactions",
                        "room_id": message["room_id"],
                        "message_id": message["_id"],
                        "thread_message_id": current_thread_message[0]["_id"],
                        "data": {
                            "reactions": current_thread_message[0]["reactions"],
                        },
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(data="No such thread message", status=status.HTTP_404_NOT_FOUND)
        return Response("No such message or room", status=status.HTTP_404_NOT_FOUND)

    def post(self, request, org_id: str, room_id: str, message_id: str, thread_message_id: str):
        request.data["message_id"] = thread_message_id
        serializer = EmojiSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            thread_message_id = data["message_id"]
            sender_id = data["sender_id"]
            data_storage = DataStorage()
            data_storage.organization_id = org_id
            
            # fetch message related to that reaction
            message = data_storage.read("dm_messages", {"_id": message_id, "room_id": room_id})
            if message:
                if "status_code" in message:
                    return Response(
                    data="Unable to retrieve data from zc core", 
                    status=status.HTTP_424_FAILED_DEPENDENCY
                    )
                # get reactions
                current_thread_message = [thread for thread in message["threads"] if thread["_id"] == thread_message_id]
                if current_thread_message:
                    reactions = current_thread_message[0].get("reactions", [])
                    data["_id"] = str(uuid.uuid1())
                    reactions.append(data)
                    # update reactions for a message
                    response = data_storage.update("dm_messages", message_id, {"threads": message["threads"]})
                    if response.get("status", None) == 200:
                        response_output = {
                            "status": response["message"],
                            "event": "add_thread_message_reaction",
                            "reaction_id": data["_id"],
                            "parent_message_id": message["_id"],
                            "thread_message_id": current_thread_message[0]["_id"],
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
                            data="Centrifugo server not available", 
                            status=status.HTTP_424_FAILED_DEPENDENCY
                            )
                    return Response(
                        "Data not sent", status=status.HTTP_424_FAILED_DEPENDENCY
                    )
                return Response(data="Not such thread message", status=status.HTTP_404_NOT_FOUND)
            return Response(
                "Message or room not found", status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )  



@api_view(["DELETE"])
@db_init_with_credentials
def delete_thread_emoji_reaction(request, room_id, message_id, thread_message_id, reaction_id):
    if request.method == "DELETE":
        message = DB.read("dm_messages", {"_id": message_id, "room_id": room_id})
        if message:
            if "status_code" in message:
                return Response(
                    data="Unable to retrieve data from zc core", 
                    status=status.HTTP_424_FAILED_DEPENDENCY
                )
            thread_message = [thread for thread in message["threads"] if thread["_id"] == thread_message_id]
            if thread_message:
                reactions = thread_message[0].get("reactions", [])
                for reaction in reactions:
                    try:
                        if reaction["_id"] == reaction_id:
                            emoji = reaction
                            break
                        emoji = None
                    except Exception:
                        pass
                if emoji:
                    reactions.remove(emoji)
                    response = DB.update("dm_messages", message_id, {"threads": message["threads"]})
                    if response.get("status", None) == 200:
                        response_output = {
                            "status": response["message"],
                            "event": "delete_thread_message_reaction",
                            "parent_message_id": message["_id"],
                            "data": {
                                "response": "Reaction successfully deleted"
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
                            data="Centrifugo server not available", 
                            status=status.HTTP_424_FAILED_DEPENDENCY
                        )
                    return Response(
                        "Data not sent", status=status.HTTP_424_FAILED_DEPENDENCY
                    )
                return Response(data="No such emoji reaction", status=status.HTTP_404_NOT_FOUND)
            return Response(data="No such thread message", status=status.HTTP_404_NOT_FOUND)
        return Response(data="Message or room not found", status=status.HTTP_404_NOT_FOUND)
    return Response(staus=status.HTTP_400_BAD_REQUEST)

