from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import UserSerializer
from .models import Message
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
	
def star_messages(request):
	star_messages = {
		'msgID': 134,
		'starred': True,
	}

	return JsonResponse(star_messages, safe=False)



def message_reminder(request):
    message_reminder = [
        {
            'sender_id': 'KFC',
            'is_ready_to_send': False,
            'Time_to_send_message': "2:01:00",
            'is_active': False,
            'is_media': False,
            'message': 'The message that you set to send some hours ago...'
        },
        {
            'sender_id': 'KFC',
            'is_ready_to_send': True,
            'Time_to_send_message': "2:01:00",
            'is_active': True,
            'is_media': True,
            'message': 'The message that you set to send some hours ago is ready to send...'
        }]
    return JsonResponse(message_reminder, safe=False)

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


def sort_message(request):
    #Use the below when the message object is ready and also delete the dummy data.
    # messages = Message.objects.order_by('-created_at')
    # messagedict = {}
    # for message_ in messagedict:
    #     messagedict['sender']=message_.sender_id
    #     messagedict['receiver']=message_.receiver_id
    #     messagedict['message']=message_.message
    #     messagedict['created_at']=message_.created_at
    #     messagedict['meta']=message_.meta
    # return  JsonResponse(messagedict)
        
    messages = [
        {
            'user': 'Fortunate',
            'location': 'Finland',
            'is_active': True,
            'message': 'Hi, dude',
            'created_at':"2020-5-10"
        },
        {
            'name': 'Asyncdeveloper',
            'location': 'Nigeria',
            'is_active': True,
            'message': 'I\'m on my way home',
            'created_at':"2021-5-10"
        }]
    return JsonResponse(messages,safe=False)

