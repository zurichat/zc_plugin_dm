from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)


def messages(request):
    messages = [
        {
            'user': 'Vitor',
            'location': 'Finland',
            'is_active': True,
            'message': 'Hi, dude'
        },
        {
            'name': 'Mykie',
            'location': 'Nigeria',
            'is_active': True,
            'message': 'I\'m on my way home'
        }]

    return JsonResponse(messages, safe=False)

# Gives information about the plugin
def info(request):
    info = {
        "message": "Plugin Information Retrieved",
        "data": {
            "type": "Plugin Information",
            "plugin_info": {"name": "DM Plugin",
                            "description": ["Zuri.chat plugin", "DM plugin for Zuri Chat that enables users to send direct messages to each other"]
                            },
            "scaffold_structure": "Monolith",
            "team": "HNG 8.0/Team Orpheus",
            "sidebar_url": "https://dm.zuri.chat/api/sideBar",
            "homepage_url": "https://dm.zuri.chat"
        },
        "success": "true"
    }
    return JsonResponse(info, safe=False)



def side_bar(request):
    pass




def organizations(request):
    organizations = [
        {
            'name': 'KFC',
            'location': 'Finland',
            'is_active': True,
            'about': 'Fast food'
        },
        {
            'name': 'Shoprite',
            'location': 'Nigeria',
            'is_active': True,
            'about': 'Supermarket'
        }]

    return JsonResponse(organizations, safe=False)

def organization(request):
    pass

def users(request):
    pass

def user(request):
    pass

def rooms(request):
    pass

def room(request):
    pass

def room_users(request):
    pass

def room_messages(request):
    pass

def room_message(request):
    pass

def room_medias(request):
    pass

def room_media(request):
    pass

def room_files(request):
    pass

def room_file(request):
    pass
