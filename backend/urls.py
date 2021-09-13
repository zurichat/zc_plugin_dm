from . import views
from django.urls import path

app_name = 'backend'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/info', views.info, name='plugin_info'),
    path('api/v1/sidebar', views.side_bar, name='sidebar'),
    path('api/v1/sendmessage', views.send_message, name="send_data"),
    path('api/v1/createroom', views.create_room, name='createroom'),
    path('api/v1/getuserrooms', views.getUserRooms, name="get_user_rooms"),
    path('api/v1/room-info', views.room_info, name='roominfo'),
    path('api/v1/getroommessages', views.getRoomMessages, name="room_messages"),
]
