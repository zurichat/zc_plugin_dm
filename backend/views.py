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
    users = [
        {
            'name': 'Seye Olowo',
            'is_active': True,
            'last_message_snippet': 'How are you man?',
            'user_info': {
                'username': 'blaco',
                'id': 1,
                'email': 'blac@gmail.com'
            }
        },
        {
            'name': 'Roman Reigns',
            'is_active': False,
            'last_message_snippet': 'Have you made your pull request?',
            'user_info': {
                'username': 'Romanric',
                'id': 12,
                'email': 'roman@gmail.com'
            }
        },
        {
            'name': 'Florence Girl',
            'is_active': True,
            'last_message_snippet': 'Thank You...',
            'user_info': {
                'username': 'Fae',
                'id': 14,
                'email': 'florence@gmail.com'
            }
        },
        {
            'name': 'Timmy Joe',
            'is_active': False,
            'last_message_snippet': 'Good evening boss, I want....',
            'user_info': {
                'username': 'manofmind',
                'id': 4,
                'email': 'timmy@gmail.com'
            }
        },
        {
            'name': 'Jeff Jones',
            'is_active': True,
            'last_message_snippet': 'My king',
            'user_info': {
                'username': 'Jiggy',
                'id': 6,
                'email': 'jonzy@gmail.com'
            }
        },
        {
            'name': 'Mamba Joy',
            'is_active': True,
            'last_message_snippet': 'i dey go school now',
            'user_info': {
                'username': 'mamba',
                'id': 100,
                'email': 'ogblaq@gmail.com'
            }
        },
        {
            'name': 'Destiny Delight',
            'is_active': False,
            'last_message_snippet': 'Good day to you, I want to ask a que.....',
            'user_info': {
                'username': 'Delight',
                'id': 189,
                'email': 'delight@gmail.com'
            }
        },
    ]

    return JsonResponse({'users': users})

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
