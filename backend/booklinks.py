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
    request_body=BookmarkSerializer,
    operation_summary="Saves links as bookmarks in a room",
    responses={400: "Error: Bad Request"},
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
        bookmarks = room.get("bookmarks", [])
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    if serializer.is_valid() and bookmarks is not None:
        # if link already bookmarked, perform an update else create new
        bookmark = [
            bookmark
            for bookmark in bookmarks
            if bookmark["link"] == serializer.data["link"]
        ]
        if bookmark:
            bookmarks.remove(bookmark[0])
            bookmark[0].update(serializer.data)
            bookmarks.append(bookmark[0])
        else:
            bookmarks.append(serializer.data)

        data = {"bookmarks": bookmarks}
        response = DB.update("dm_rooms", room_id, data=data)
        if response.get("status") == 200:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["get"],
    operation_summary="Retrieves all bookmarks in a room",
    responses={200: BookmarkResponse, 400: "Error: Bad Request"},
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



@swagger_auto_schema(
    methods=["delete"],
    operation_summary="Deletes bookmarks from rooms",
    responses={
        200: "OK: Success",
        400: "Error: Bad Request",
        503: "Server Error: Service Unavailable",
    },
)
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
    if bookmarks is not None:
        name = request.query_params.get("name", "")
        for bookmark in bookmarks:
            if name == bookmark.get("name", ""):
                bookmarks.remove(bookmark)
                break
        data = {"bookmarks": bookmarks}
        response = DB.update("dm_rooms", room_id, data=data)
        if response.get("status") == 200:

            centrifuge_data ={
                "room_id" : room_id,
                "bookmark_name" : name,
                "event" : "bookmark_delete"
            }

            centrifugo_response = centrifugo_client.publish(room=room_id, data=centrifuge_data)

            if centrifugo_response and centrifugo_response.get("status_code") == 200:
                return Response(status=status.HTTP_200_OK)
            return Response("Centrifugo failed", status=status.HTTP_424_FAILED_DEPENDENCY)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(
    methods=["get"],
    operation_summary="Retrieves the link to a message",
    responses={
        200: MessageLinkResponse,
        400: "Error: Bad Request",
        404: "Error: This Message Does Not Exist",
    },
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
        return Response(
            data="The message does not exist", status=status.HTTP_404_NOT_FOUND
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
        message = DB.read("dm_messages", {"id": message_id, "room_id": room_id})
        return Response(data=message, status=status.HTTP_200_OK)
    else:
        return JsonResponse(
            {"message": "The message does not exist"}, status=status.HTTP_404_NOT_FOUND
        )


@swagger_auto_schema(
    methods=["get"],
    operation_summary="Retrieves all the links in a room",
    responses={
        200: GetLinksResponse,
        404: "Error: Message Not Found",
    },
)
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
                        {"link": str(word), "timestamp": message.get("created_at")}
                    )
        data = {"links": matches, "room_id": room_id}
        return Response(data=data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)