from .import views
from .testingapi import Test
# from .views import EditMessage
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("api/v1/info", views.info, name="plugin_info"),
    path("api/v1/sidebar", views.side_bar, name="sidebar"),
    path("api/v1/org/<str:org_id>/rooms/<str:room_id>/messages", views.send_message, name="send_message"),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads",
        views.send_thread_message,
        name="send_thread_message",
    ),
    path(
        "api/v1/<str:org_id>/createroom",
        views.create_room,
        name="createroom"
    ),
    path(
        "api/v1/<str:org_id>/updatemessage/<str:pk>",
        views.edit_room,
        name="updateroom"
    ),
    path(
        "api/v1/<str:org_id>/room-info",
        views.room_info,
        name="roominfo"
    ),
    path(
        "api/v1/<str:org_id>/<str:user_id>/rooms",
        views.getUserRooms,
        name="get_user_rooms"
    ),
    path(
        "api/v1/<str:org_id>/reminder",
        views.remind_message,
        name="reminder"
    ),
    # path('api/v1/getroommessages', views.getRoomMessages, name="room_messages"),
    path(
        "api/v1/<str:org_id>/<str:room_id>/messages",
        views.room_messages,
        name="room_messages"
    ),
    path(
        "api/v1/<str:org_id>/copymessagelink/<str:message_id>",
        views.copy_message_link,
        name="copy_message_link",
    ),
    path(
        "getmessage/<str:room_id>/<str:message_id>",
        views.read_message_link,
        name="read_message_link",
    ),
    path(
        "api/v1/<str:org_id>/<str:room_id>/links",
        views.get_links,
        name="get_links"
    ),
    path(
        "api/v1/<str:org_id>/<str:room_id>/bookmark/new",
        views.save_bookmark,
        name="create_bookmark"
    ),
    path(
        "api/v1/organization/<str:org_id>/members",
        views.organization_members,
        name="organization_members",
    ),
    path(
        "api/v1/<str:org_id>/<str:room_id>/bookmark/all",
        views.retrieve_bookmarks,
        name="get_bookmarks",
    ),
    path(
        "api/v1/<str:org_id>/<str:message_id>/read/new",
        views.mark_read,
        name="mark_read"
    ),
    path(
        "api/v1/<str:org_id>/messages/<str:message_id>/pin",
        views.pinned_message,
        name="pin_message",
    ),
    path(
        "api/v1/<str:org_id>/messages/<str:message_id>/unpin",
        views.delete_pinned_message,
        name="unpin_message",
    ),
    path(  # is this getting a single pinned message or all pinned message in a room???
        "api/v1/<str:org_id>/<str:room_id>/<str:message_id>/pinnedmessage/",
        views.read_message_link,
        name="read_pinned_message",
    ),
    path(
        "api/v1/<str:org_id>/<str:room_id>/filter_messages",
        views.message_filter,
        name="message_filter",
    ),
    # Deleting a message without :room_id and :message_id, why???
    path("api/v1/delete-message/<str:message_id>/",
         views.delete_message, name="delete_message"),
    path(
        "api/v1/<str:org_id>/members/<str:member_id>/profile",
        views.user_profile,
        name="user_profile",
    ),
    path(  # give a descriptive name to this route not just "view"
        "api/v1/<str:org_id>/rooms/<str:room_id>/messagemedia",
        views.SendFile.as_view(),
        name="view"
    ),
    path(
        "api/v1/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/reactions",
        views.Emoji.as_view(),
        name="message_reactions",
    ),
    path("api/v1/testapi/<str:plugin_id>", Test.as_view(), name="testview"),
    path("api/v1/org/<str:org_id>/message/schedule", views.scheduled_messages, name="scheduled_messages"),


    path(
        "api/v1/<str:org_id>/<str:room_id>/bookmark/delete",
        views.delete_bookmark,
        name="delete_bookmark"
    ),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
