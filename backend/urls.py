from . import views
from django.urls import path

app_name = 'backend'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/info', views.info, name='plugin_info'),
    path('api/v1/sidebar', views.side_bar, name='sidebar'),
    path('api/v1/sendmessage', views.send_message, name="send_message"),
    path('api/v1/sendthreadmessage', views.send_thread_message, name="send_thread_message"),
    path('api/v1/createroom', views.create_room, name='createroom'),
    path('api/v1/updatemessage/<str:pk>', views.edit_room, name='updateroom'),
    path('api/v1/room-info', views.room_info, name='roominfo'),
    path('api/v1/getuserrooms', views.getUserRooms, name="get_user_rooms"),
    path('api/v1/room-info', views.room_info, name='roominfo'),
    path('api/v1/getroommessages', views.getRoomMessages, name="room_messages"),
    path('api/v1/copymessagelink/<str:message_id>', views.copy_message_link, name="copy_message_link"),
    path('getmessage/<str:room_id>/<str:message_id>', views.read_message_link, name="read_message_link"),
    path('api/v1/<str:room_id>/links', views.get_links, name="get_links"),
    path('api/v1/<str:room_id>/bookmark/new', views.save_bookmark, name="create_bookmark"),
]
