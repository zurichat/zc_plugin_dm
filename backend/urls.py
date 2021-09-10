from . import views
from django.urls import path

app_name = "backend"

urlpatterns = [
    path("", views.index, name="index"),
    path("api/info", views.info, name="plugin_info"),
    path("api/v1/sidebar", views.side_bar, name="sidebar"),
    path("api/organizations", views.organizations, name="organizations"),
    path("api/organizations/id", views.organization, name="organization"),
    path("api/organizations/id/users", views.users, name="users"),
    path("api/organizations/id/users/id", views.user, name="user"),
    path("api/organizations/id/rooms", views.rooms, name="rooms"),
    path("api/organizations/id/rooms/id", views.room, name="room"),
    path("api/organizations/id/rooms/id/users/", views.room_users, name="room_users"),
    path(
        "api/organizations/id/rooms/id/messages",
        views.room_messages,
        name="room_messages",
    ),
    path(
        "api/organizations/id/rooms/id/messages/id",
        views.room_message,
        name="room_message",
    ),
    path("api/organizations/id/rooms/id/media", views.room_medias, name="room_medias"),
    path("api/organizations/id/rooms/id/media/id", views.room_media, name="room_media"),
    path("api/organizations/id/rooms/id/files", views.room_files, name="room_files"),
    path("api/organizations/id/rooms/id/files/id", views.room_file, name="room_file"),
]
