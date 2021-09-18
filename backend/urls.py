from requests.api import delete
from . import views
# from .views import EditMessage
from django.urls import path

app_name = "backend"

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/info', views.info, name='plugin_info'),
    path('api/v1/sidebar', views.side_bar, name='sidebar'),
    path('api/v1/rooms/<str:room_id>/message', views.send_message, name="send_message"),
    path('api/v1/rooms/<str:room_id>/messages/<str:message_id>/thread', views.send_thread_message, name="send_thread_message"),
    path('api/v1/createroom', views.create_room, name='createroom'),
    path('api/v1/updatemessage/<str:pk>', views.edit_room, name='updateroom'),
    path('api/v1/room-info', views.room_info, name='roominfo'),
    path('api/v1/getuserrooms', views.getUserRooms, name="get_user_rooms"),
    path('api/v1/reminder', views.remind_message, name='reminder' ),
    path('api/v1/getroommessages', views.getRoomMessages, name="room_messages"),
    path('api/v1/copymessagelink/<str:message_id>', views.copy_message_link, name="copy_message_link"),
    path('getmessage/<str:room_id>/<str:message_id>', views.read_message_link, name="read_message_link"),
    path('api/v1/<str:room_id>/links', views.get_links, name="get_links"),
    path('api/v1/<str:room_id>/bookmark/new', views.save_bookmark, name="create_bookmark"),
    path('api/v1/get_organization_members', views.organization_members, name="organization_members"),
    path('api/v1/<str:room_id>/bookmark/all', views.retrieve_bookmarks, name="get_bookmarks"),
    path('api/v1/<str:message_id>/read/new/', views.mark_read, name="mark_read"),
    path('api/v1/<str:message_id>/pinnedmessages/new', views.pinned_message, name="pinned_message"),
    path('api/v1/<str:message_id>/deletepinnedmessage/', views.delete_pinned_message, name="pinned_message"),
    path('api/v1/<str:room_id>/<str:message_id>/pinnedmessage/', views.read_message_link, name="read_pinned_message"),
    path('api/v1/<str:room_id>/filter_messages', views.message_filter, name="message_filter"),
    path('api/v1/delete-message', views.delete_message, name="delete_message"),
    path('api/v1/<str:org_id>/users/<str:user_id>', views.user_profile, name="user_profile")

]
