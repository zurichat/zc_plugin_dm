import json, uuid, re
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework import status
import requests
from .db import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.core.files.storage import default_storage


class Test(APIView):
    parser_classes = (
        MultiPartParser, FormParser
    )

    def post(self, request, plugin_id):
        files = request.FILES
        files = request.FILES.getlist('file')
        if len(files)==1:
            for file in request.FILES:
                file = request.FILES["file"]
                filename = default_storage.save(file.name, file)
                file_url = default_storage.url(filename)

               
                response =  {
                        "status":200,
                        "message":"File Upload Successful",
                        "data" : {
                            "file_url": file_url,
                            "status": True
                        }
                    }
                return Response(response)
        elif len(files)>1:
            response = {
                        "status":200,
                        "message":"File Upload Successful",
                        "data" : {
                            "files_info": []
                        }
                    }
            for file in files:
                filename = default_storage.save(file.name, file)
                file_url = default_storage.url(filename)
                data = {
                    "original_name": file.name,
                    "file_url":file_url
                }
                response["data"]["files_info"].append(data)
            return Response(response)
