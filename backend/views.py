from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import UserSerializer

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

def new_messages(request):
    messages = [
        {
            'id': '10',
            'sender_id': '1',
            'receiver_id': '2',
            'message': 'Hi, dude',
            'meta': 'dm_message_304303848',
            'deleted_user_id': 'null',
            'created_at': '2021,9,2,0,0',
            'last_updated_at': 'null',
        },
        {
            'id': '11',
            'sender_id': '1',
            'receiver_id': '2',
            'message': 'Its been awhile',
            'meta': 'dm_message_304303849',
            'deleted_user_id': 'null',
            'created_at': '2021,9,1,0,0',
            'last_updated_at': 'null',
        }]

    return JsonResponse(messages, safe=False)


def info(request):
    info = {
        'plugin_id': 201982982,
        'plugin_name': 'DM plugin',
        'about': 'serves the ability for users to send messages to each other privately'
    }


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
