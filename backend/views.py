from .models import Message
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework.decorators import api_view

from .serializers import UserSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)


def forward_messages(request):
    forwarded_messages = [
        {
            'user': 'Itz_salemm',
            'location': 'Switzerland',
            'forwarded_to': ['mark', ],
            'forward': True
        },
        {
            'user': 'Samuel',
            'location': 'UK',
            'forwarded_to': ['naza', ],
            'forward': True
        }
    ]

    return JsonResponse(forwarded_messages, safe=False)


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

    return HttpResponse(f"{messages}")


def new_messages(request):
    messages = [
        {
            'id': '1',
            'sender_id': '5',
            'receiver_id': '4',
            'message': 'been awhile',
            'meta': 'dm_message38384739',
            'deleted_user_id': 'null',
            'created_at': '2021-09-3 00:00:00',
            'last_updated_at': 'null'
        },
        {
            'id': '1',
            'sender_id': '5',
            'receiver_id': '4',
            'message': 'Hi, dude',
            'meta': 'dm_message38384738',
            'deleted_user_id': 'null',
            'created_at': '2021-09-2 00:00:00',
            'last_updated_at': 'null'
        }]

    return HttpResponse(f"{messages}")


def side_bar(request):
    pass


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


def archive_message(request):
    archive_message = {
        'msgID': 121,
        'archived': True
    }
    return JsonResponse(archive_message, safe=False)


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


def list_archives(request):
    archived_messages = [
        {
            'id': '13',
            'from': 'Korede',
            'to': ['mark', ],
            'message': 'Are you now in stage 5?',
            'date_sent': '2021-05-15T10:49:59.581770Z',
            'archived': True
        },
        {
            'id': '21',
            'from': 'Xylum',
            'to': ['KoredeDavid', ],
            'date_sent': '2021-05-17T18:27:24.376865Z',
            'message': 'I need your help sir',
            'archived': True
        }
    ]

    return JsonResponse(archived_messages, safe=False)


def organization(request):
    return HttpResponse("<h1>Is this working?</h1>")


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


def user_profile(request):
    user_profile = [
        {
            'username': 'Derin',
            'fullname': 'Derin Aslin',
            'image': 'templates/images/big.jpg',
            'email': 'derino@zuri.com',
            'date joined': '22/08/2021',

        }
    ]
    return JsonResponse(user_profile, safe=False)


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
    # Use the below when the message object is ready and also delete the dummy data.
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
            'created_at': "2020-5-10"
        },
        {
            'name': 'Asyncdeveloper',
            'location': 'Nigeria',
            'is_active': True,
            'message': 'I\'m on my way home',
            'created_at': "2021-5-10"
        }]
    return JsonResponse(messages, safe=False)


@api_view(['GET'],)
def star_messages(request):
    star_messages = {
        'msgID': 134,
        'starred': True,
    }

    return Response(star_messages, status=status.HTTP_200_OK)


@api_view(['GET'], )
def auto_response(request):
    auto_response_message = {
        'userId': 23,
        'auto_response': True,
        'message': "Brian is currently offline. Please leave your message. He will reply you as soon as he's back "
                   "online "
    }

    return Response(auto_response_message, status=status.HTTP_200_OK)


@api_view(['GET'])
def send_media(request):
    media = [
        {
            # original message being sent
            "message":
            {
                "attachment": {
                    "type": "image",
                    "payload": {
                        # makes it possible to send the media file to another person via the app
                        "is_reusable": True
                    }
                },
                "mediaLocation": "./media/funny.jpeg",
                "type": "image/png"
            },
        }
    ]
    return Response(media, status=status.HTTP_200_OK)


@api_view(['GET'],)
def pagination(request):
    limit = int(request.query_params.get('limit', 2))
    page = int(request.query_params.get('page', 1))
    total_messages = {
        "page": page,
        "limit": limit,
        "messages":   [
            {
                'sender': 'Victor',
                'receiver': 'Samuel',
                'message': 'Hello, dude',
                'seen': True
            },
            {
                'sender': 'Samuel',
                'receiver': 'Vctor',
                'message': 'Hello!!!',
                'seen': True
            },
            {
                'sender': 'Victor',
                'receiver': 'Samuel',
                'message': 'How was today ?',
                'seen': True
            },
            {
                'sender': 'Samuel',
                'receiver': 'Victor',
                'message': 'Good, good!!!, Yours ?',
                'seen': True
            },
            {
                'sender': 'Victor',
                'receiver': 'Samuel',
                'message': 'Great',
                'seen': True
            },
            {
                'sender': 'Samuel',
                'receiver': 'Victor',
                'message': 'How was your day',
                'seen': True
            },
            {
                'sender': 'Victor',
                'receiver': 'Samuel',
                'message': 'Fine',
                'seen': True
            }
        ]
    }

    if limit > 7:
        return Response("Limit cannot exceed number of messages", status=status.HTTP_400_BAD_REQUEST)
    else:
        total_messages['messages'] = total_messages["messages"][page-1:page+limit-1:]
        return Response(total_messages, status=status.HTTP_200_OK)


# get delete and post for messages view task
# 1 for individual message using id
@api_view(['GET', 'PUT', 'DELETE'])
def message_detail(request, pk):
    try:
        text = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return JsonResponse({'message': 'The message does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        message_serializer = MessageSerializer(text)
        return JsonResponse(message_serializer.data)

    elif request.method == 'PUT':
        message_data = JSONParser().parse(request)
        mess_serializer = MessageSerializer(text, data=message_data)
        if mess_serializer.is_valid():
            mess_serializer.save()
            return JsonResponse(mess_serializer.data)
        return JsonResponse(mess_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        text.delete()
        return JsonResponse({'message': 'Your text was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    # 2. Deleting multiple messages at once or updating


@api_view(['GET', 'POST', 'DELETE'])
def message_list(request):
    if request.method == 'GET':
        messag = Message.objects.all()

        text = request.query_params.get('message', None)

        messag_serializer = MessageSerializer(messag, many=True)
        return JsonResponse(messag_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        messag_data = JSONParser().parse(request)
        messag_serializer = MessageSerializer(data=messag_data)
        if messag_serializer.is_valid():
            messag_serializer.save()
            return JsonResponse(messag_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(messag_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Message.objects.all().delete()
        return JsonResponse({'message': '{} messages were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def send_file(request):
    file = [
        {

            'id': '1',
            'message_id': '2',
            'file_name': 'dbdiagram',
            'file_path': 'media/dbdiagram.pdf',
            'created_at': '20-09-21 19:03:01'
        }
    ]
    return Response(file, status=status.HTTP_200_OK)


@api_view(['GET'],)
def replyMessage(request):
    messageList = {
        "message1": [{
            "message_id": "001",
            "user": "Mykie",
            "content": "Hello Mark"
        }],
        "message2": [{
            "message_id": "002",
            "user": "Mark",
            "content": "Hi Mykie, how are you doing?"
        }]
    }
    mesSage = messageList["message2"]
    reply_message = [
        {
            'reply_id': "003",
            'replied_to': mesSage,
            'content': 'I am fine Mark thank you',
        }
    ]
    return Response(reply_message, status=status.HTTP_200_OK)


def dm_list(request):
    dm_lists = [{"user": "Cheeqito", "isActive": True, "last_message": "10 minutes Ago"},
                {"user": "Cheediogo", "isActive": False,
                    "last_message": "2Hours Ago"},
                {"user": "James", "isActive": True, "last_message": "2 minutes Ago"}, ]
    return JsonResponse(dm_lists, safe=False)


def filter_user(request):
    filter_user = [
        {
            'user_id': '1',
            'message': 'Hey, how are you doing'
        },

        {
            'user_id': '1',
            'message': 'I need to have some rest'
        },

        {
            'user_id': '1',
            'message': 'I would see you later'
        }
    ]

    return JsonResponse(filter_user, safe=False)


@api_view(['GET'],)
def get_starred(request):
    get_starred = [
        {
            'sender_id': 'Laurie',
            'message': 'Hello',
            'created_at': '0800hrs',
            'star_messages': True,
        },

        {
            'sender_id': 'Barney',
            'message': 'Assignment due',
            'created_at': '1500hrs',
            'star_messages': True,
        }

    ]
    return JsonResponse(get_starred, safe=False)


def edit_message(request):
    messages = [{
        'user_id': '2',
        'message_id': '34',
        'last_updated': '2021-09-04 19:11:35',
        'message': 'I just edited this message'

    }]
    return JsonResponse(messages, safe=False)


class SearchMessagesAPI(APIView):
    def get_match(self, phrase):
        try:
            # here we serch through the messages for a phrase.
            pass
        except Exception as e:
            pass

    def get(self, request, phrase):
        # we search the message
        matchedMessages = self.get_match(phrase)

        # expected outcome for the phrase home
        matchedMessages = [
            {
                'message_id': '1',
                'name': 'Vitor',
                'message': 'home is where my heart is.'
            },
            {
                'message_id': '65',
                'name': 'Mykie',
                'message': 'I\'m on my way home'
            },
            {
                'message_id': '8',
                'name': 'john',
                'message': 'home file.'
            }]
        return Response(matchedMessages, status=status.HTTP_200_OK)


def date_message(request):
    '''
    Returns filtered messages between a date range: [before date] and [after date]
    '''

    results = [
        {
            'user_id': 'Mark',
            'message': 'Hello',
            'created_at': '2021-09-01 04:20:35',
            'date_timestamps': 1538697600
        },
        {
            'user_id': 'Oluwaseye',
            'message': 'Assignment due',
            'created_at': '2021-09-01 06:15:14',
            'date_timestamps': 1538697500

        },
        {
            'user_id': 'Oluwaseye',
            'message': 'They are the best',
            'created_at': '2021-09-01 08:15:14',
            'date_timestamps': 1538297500
        },
        {
            'user_id': 'Mark',
            'message': 'Restart the server',
            'created_at': '2021-09-01 09:15:14',
            'date_timestamps': 1538297900
        },

    ]
    return JsonResponse(results, safe=False)


def search_users(request):
    contacts = [
        {"username": ["Alan ", "Bola", "Chris", "Duke"]},
        {
            "letters": {
                {"a": ["Alan", "Alex", "Andrew"]},
                {"b": ["Betty", "Bola", "Bella"]},
                {"c": ["Cate", "Chris", "Cinda"]},
                {"d": ["Dave", "Duke", "Dorathy"]}
            }
        }
    ]
    return JsonResponse(contacts, safe=False)
  
  
@api_view(['GET'], )
def filter_keywords(request):
    keyword = "tomorrow"
    queryset = [
            {
                'sender': 'Groot',
                'message': 'Hello, dude! can we meet tomorrow?',
            },
            {
                'sender': 'Florence',
                'message': 'Hello!!! I know what you are doing',
            },
            {
                'sender': 'Grace',
                'message': 'I have no plans for tomorrow',
            },
            {
                'sender': 'Samuel',
                'message': 'Good, good!!!, Yours ?',
            },
            {
                'sender': 'Maria',
                'message': 'Great',
            },
            {
                'sender': 'Samuel',
                'message': 'How was your day'
            },
            {
                'sender': 'Victor',
                'message': 'Fine'
            }
    ]

    filtered = [
        {
                'sender': 'Groot',
                'message': 'Hello, dude! can we meet tomorrow?',
        },

        {
            'sender': 'Grace',
            'message': 'I have no plans for tomorrow',
        },
    ]

    return JsonResponse(filtered, safe=False)

def pinned_messages(request):
    pinned_messages = [
      {
           'user': 'tonye',
           'is_active': True,
           'pinned_message': 'I am home'
      },
      {
           'user': 'praise',
           'is_active': True,
           'pinned_message': 'avoid Canada'
      }]
    return JsonResponse(pinned_messages, safe=False)