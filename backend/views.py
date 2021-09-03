from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import UserSerializer
from .models import User , profile_image


# Create your views here.


def index(request):
    context = {}
    return render ( request , 'index.html' , context )


def messages(request):
    messages = [
        {
            'user': 'Vitor' ,
            'location': 'Finland' ,
            'is_active': True ,
            'message': 'Hi, dude'
        } ,
        {
            'name': 'Mykie' ,
            'location': 'Nigeria' ,
            'is_active': True ,
            'message': 'I\'m on my way home'
        }]

    return JsonResponse ( messages , safe=False )


def info(request):
    info = {
        'plugin_id': 201982982 ,
        'plugin_name': 'DM plugin' ,
        'about': 'serves the ability for users to send messages to each other privately'
    }


def organizations(request):
    organizations = [
        {
            'name': 'KFC' ,
            'location': 'Finland' ,
            'is_active': True ,
            'about': 'Fast food'
        } ,
        {
            'name': 'Shoprite' ,
            'location': 'Nigeria' ,
            'is_active': True ,
            'about': 'Supermarket'
        }]

    return JsonResponse ( organizations , safe=False )


def organization(request):
    pass


def users(request):
    pass


def user(request):
    pass


def user_profile(request):
    user_profile = [
        {
            'username': get_username () ,
            'fullname': get_full_name () ,
            'image': image,
            'email': get_email_user () ,
            'date joined': get_date_joined () ,

        }
    ]
    return JsonResponse ( user_profile , safe=False )


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
