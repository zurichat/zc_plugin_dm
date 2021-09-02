from . import views
from django.urls import path

app_name = 'backend'

urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info, name='info'),
    path('api/organizations', views.organizations, name='organizations'),
    path('api/organizations/id', views.organization, name='organization'),
    path('api/organizations/id/users', views.users, name='users'),
    path('api/organizations/id/users/id', views.user, name='user'),
    path('api/organizations/id/rooms', views.rooms, name='rooms'),
    path('api/organizations/id/rooms/id', views.room, name='room'),
    path('api/organizations/id/rooms/id/users/', views.room_users, name='room_users'),
    path('api/organizations/id/rooms/id/messages', views.room_messages, name='room_messages'),
    path('api/organizations/id/rooms/id/messages/id', views.room_message, name='room_message'),
    path('api/organizations/id/rooms/id/media', views.room_medias, name='room_medias'),
    path('api/organizations/id/rooms/id/media/id', views.room_media, name='room_media'),
    path('api/organizations/id/rooms/id/files', views.room_files, name='room_files'),
    path('api/organizations/id/rooms/id/files/id', views.room_file, name='room_file'),

    # Specific Routes for tasks
    path('api/users',views.index),
    path('api/newMessages',views.index),
    path('api/searchUser',views.index),
    path('api/messages',views.index),
    path('api/starMessage',views.index),
    path('api/starredMessages',views.index),
    path('api/sendFile',views.index),
    path('api/sendMedia',views.index),
    path('api/messagesByDate',views.index),
    path('api/messageByUser',views.index),
    path('api/messageByKeywords',views.index),
    path('api/pagination',views.index),
    path('api/userProfile',views.index),
    path('api/editUserProfile',views.index),
    path('api/forwardMessages',views.index),
    path('api/replyMessage',views.index),
    path('api/userStatus',views.index),
    path('api/DMList',views.index),
    path('api/pinMessage',views.index),
    path('api/pinnedMessages',views.index),
    path('api/archiveMessage',views.index),
    path('api/archivedMessages',views.index),
    path('api/editMessage',views.index),
    path('api/deleteMessage',views.index),
    path('api/sortMessage',views.index),
    path('api/autoResponse',views.index),
    path('api/setReminder',views.message_reminder, name = "message_reminder"),



    path('messages', views.messages, name='messages'),

]
