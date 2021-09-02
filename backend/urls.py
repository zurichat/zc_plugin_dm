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
    path('api/user'),
    path('api/newMessages'),
    path('api/searchUser'),
    path('api/messages'),
    path('api/starMessage'),
    path('api/starredMessages'),
    path('api/sendFile'),
    path('api/sendMedia'),
    path('api/messagesByDate'),
    path('api/messageByUser'),
    path('api/messageByKeywords'),
    path('api/pagination'),
    path('api/userProfile'),
    path('api/editUserProfile'),
    path('api/forwardMessages'),
    path('api/replyMessage'),
    path('api/userStatus'),
    path('api/DMList'),
    path('api/pinMessage'),
    path('api/pinnedMessages'),
    path('api/archiveMessage'),
    path('api/archivedMessages'),
    path('api/editMessage'),
    path('api/deleteMessage'),
    path('api/sortMessage'),
    path('api/autoResponse'),
    path('api/setReminder'),
    


    path('messages', views.messages, name='messages'),

]
