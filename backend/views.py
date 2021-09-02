from backend.models import Message
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
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

    
@api_view(['GET'],)
def pagination(request):
    limit = int(request.query_params.get('limit', 2))
    page = int(request.query_params.get('page', 1))
    total_messages = {
        "page":page,
        "limit":limit,
         "messages":   [
            {
                'sender': 'Victor',
                'receiver': 'Samuel',
                'message': 'Hello, dude',
                'seen':True
            },
            {
                'sender': 'Samuel',
                'receiver': 'Vctor',
                'message': 'Hello!!!',
                'seen':True
            },
                {
                'sender': 'Victor',
                'receiver': 'Samuel',
                'message': 'How was today ?',
                'seen':True
            },
            {
                'sender': 'Samuel',
                'receiver': 'Victor',
                'message': 'Good, good!!!, Yours ?',
                'seen':True
            },
            {
                'sender': 'Victor',
                'receiver': 'Samuel',
                'message': 'Great',
                'seen':True
            },
            {
                'sender': 'Samuel',
                'receiver': 'Victor',
                'message': 'How was your day',
                'seen':True
            },
            {
                'sender': 'Victor',
                'receiver': 'Samuel',
                'message': 'Fine',
                'seen':True
            }
        ]
            }
    
    if limit > 7:
        return Response("Limit cannot exceed number of messages", status=status.HTTP_400_BAD_REQUEST)
    else:
        total_messages['messages'] = total_messages["messages"][page-1:page+limit-1:]
        return Response(total_messages, status=status.HTTP_200_OK)
        
    
    
