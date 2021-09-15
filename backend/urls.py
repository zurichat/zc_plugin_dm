from . import views
# from .views import EditMessage
from django.urls import path
from django.views.decorators import csrf_exempt

app_name = 'backend'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/info', views.info, name='plugin_info'),
    path('api/v1/sidebar', views.side_bar, name='sidebar'),
    path('api/v1/send-data', views.send_message, name="send_data"),
    path('api/v1/createroom', views.create_room, name='createroom'),
    path('api/v1/getuserrooms', views.getUserRooms, name="get_user_rooms"),
    path('api/v1/room-info', views.room_info, name='roominfo'),
    path('api/v1/reminder', csrf_exempt(views.reminder), name='reminder' )
]
