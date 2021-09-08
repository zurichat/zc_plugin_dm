from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



def index(request):
    context = {}
    return render(request, 'index.html', context)


def info(request):
    info = {
        "message": "Plugin Information Retrieved",
        "data": {
            "type": "Plugin Information",
            "plugin_info": {"name": "DM Plugin",
                            "description": ["Zuri.chat plugin", "DM plugin for Zuri Chat that enables users to send messages to each other"]
                            },
            "scaffold_structure": "Monolith",
            "team": "HNG 8.0/Team Orpheus",
            "sidebar_url": "https://dm.zuri.chat/api/sideBar",
            "homepage_url": "https://dm.zuri.chat/"
        },
        "success": "true"
    }

    return JsonResponse(info, safe=False)

def side_bar(request):
    side_bar = {
        "message": "DM sidebar Information Retrieved",
        "data": {
            "type": "Sidebar Information",
            "Messages": [{"user": "Abey","message":"I dey boss"},
            {"user": "Abike","message":"I dey boss"},
            {"user": "Franc","message":"How's it going"},
            {"user": "Dele","message":"Yes it is"},
            {"user": "Abey","message":"I've not slept in days"},
            ],
            "scaffold_structure": "Monolith",
            "team": "HNG 8.0/Team Orpheus",
            "info_url": "https://dm.zuri.chat/api/info",
            "homepage_url": "https://dm.zuri.chat/"
        },
        "success": "true"
    }

    return JsonResponse(side_bar, safe=False)


def organization(request):
    return render(request, "index.html")

def organizations(request):
    return render(request, "index.html")


def user(request):
    return render(request, "index.html")

def users(request):
    return render(request, "index.html")


def rooms(request):
    return render(request, "index.html")


def room(request):
    return render(request, "index.html")


def room_users(request):
    return render(request, "index.html")


def room_messages(request):
    return render(request, "index.html")


def room_message(request):
    return render(request, "index.html")


def room_medias(request):
    return render(request, "index.html")


def room_media(request):
    return render(request, "index.html")


def room_files(request):
    return render(request, "index.html")


def room_file(request):
    return render(request, "index.html")
