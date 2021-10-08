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
    operation_summary="Retrieves all the members in an organization",
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
    operation_summary="Retrieves the profile details of a user",
    responses={
        200: UserProfileResponse,
        401: "Error: Unauthorized Access",
        405: "Error: Method Not Allowed",
    },
)
@api_view(["GET"])
def user_profile(request, org_id, member_id):
    """
    Retrieves the user details of a member in an organization using a unique user_id
    If request is successful, a json output of select user details is returned
    Elif login session is expired or wrong details were entered, a 401 response is returned
    Else a 405 response returns if a wrong method was used
    Assume member_id is also the same as user_id in an org
    """

    url = f"https://api.zuri.chat/organizations/{org_id}/members/{member_id}"

    if request.method == "GET":
        header = {'Authorization': f'Bearer {login_user()}'}
        # if "Authorization" in request.headers:
        #     headers["Authorization"] = request.headers["Authorization"]
        # else:
        #     headers["Cookie"] = request.headers["Cookie"]
        response = requests.get(url, headers=header)
        
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if response.status_code == 200:
        data = response.json()["data"]
        if data["image_url"] == "":
            data["image_url"] = "https://cdn.iconscout.com/icon/free/png-256/account-avatar-profile-human-man-user-30448.png"
        if data["first_name"] == "":
            data["first_name"] = None
        if data["last_name"] == "":
            data["last_name"] = None
        if data["display_name"] == "":
            data["display_name"] = data["user_name"]
        if data["bio"] == "":
            data["bio"] = "Add Bio"
        if data["pronouns"] == "":
            data["pronouns"] = "Add Pronouns"
        if data["phone"] == "":
            data["phone"] = None
        if data["status"] == "":
            data["status"] = "Available"
        output = {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "display_name": data["display_name"],
            "user_name": data["user_name"],
            "image_url": data["image_url"],
            "bio": data["bio"],
            "pronouns": data["pronouns"],
            "email": data["email"],
            "phone": data["phone"],
            "status": data["status"],
        }
        return Response(output, status=status.HTTP_200_OK)
    return Response(response.json(), status=status.HTTP_401_UNAUTHORIZED)
