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




class SendFile(APIView):
    """
    This endpoint is a send message endpoint that can take files, upload them
    and return the urls to the uploaded files to the media list in the message
    serializer
    This endpoint uses form data
    The file must be passed in with the key "file"

    """

    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        operation_summary="Sends files as messages in rooms",
        responses={
            201: "OK: File Created!",
        },
    )
    # @method_decorator(db_init_with_credentials)
    def post(self, request, room_id, org_id):
        print(request.FILES)
        token = request.META.get("HTTP_AUTHORIZATION")
        if request.FILES:
            file_urls = []
            files = request.FILES.getlist("file")
            if len(files) == 1:
                for file in request.FILES.getlist("file"):
                    file_data = DB.upload(file=file, token=token)
                    if file_data["status"] == 200:
                        for datum in file_data["data"]["files_info"]:
                            file_urls.append(datum["file_url"])
                    else:
                        return Response(file_data)
            elif len(files) > 1:
                multiple_files = []
                for file in files:
                    multiple_files.append(("file", file))
                file_data = DB.upload_more(files=multiple_files, token=token)
                if file_data["status"] == 200:
                    for datum in file_data["data"]["files_info"]:
                        file_urls.append(datum["file_url"])
                else:
                    return Response(file_data)

            request.data["room_id"] = room_id
            print(request)
            serializer = MessageSerializer(data=request.data)

            if serializer.is_valid():
                data = serializer.data
                room_id = data["room_id"]  # room id gotten from client request

                room = DB.read("dm_rooms", {"_id": room_id})
                if room and room.get("status_code", None) == None:
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
        return Response(status=status.HTTP_400_BAD_REQUEST)
