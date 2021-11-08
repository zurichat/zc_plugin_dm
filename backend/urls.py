from backend import sync
from . import views, rooms, messaging, members, media, threads, booklinks, reactions
from .testingapi import Test

# from .views import EditMessage
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("", views.index, name="index"),
    path("api/v1/ping", views.PING, name="ping"),
    path("api/v1/info", views.info, name="plugin_info"),
    path("api/v1/install", views.dm_install, name="install"),
    path("api/v1/sidebar", views.side_bar, name="sidebar"),
    path(
        "api/v1/org/<str:org_id>/users/<str:member_id>/room",
        rooms.create_room,
        name="create_room",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/info",
        rooms.room_info,
        name="room_info",
    ),
    path(
        "api/v1/org/<str:org_id>/users/<str:user_id>/rooms",
        rooms.user_rooms,
        name="get_user_rooms",
    ),
    path(
        "api/v1/search/<str:org_id>/<str:member_id>",
        rooms.search_DM,
        name="search DM",
    ),
    path(
        "api/v1/search-suggestions/<str:org_id>/<str:member_id>",
        rooms.search_suggestions,
        name="search suggestions",
    ),
    path(
        "api/v1/org/<str:org_id>/room/<str:room_id>/members/<str:member_id>",
        rooms.group_member_add,
        name="group_user_add",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/members/<str:member_id>/close_conversation",
        rooms.close_conversation,
        name="close_conversation",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/members/<str:member_id>/star",
        rooms.star_room,
        name="star_room",
    ),
    path(
        "api/v1/org/<str:org_id>/members/<str:member_id>/all_dms",
        rooms.all_dms,
        name="all_dms",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages",
        messaging.message_create_get,
        name="create_get_message",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/schedule-message",
        messaging.scheduled_messages,
        name="scheduled_messages",
    ),
    path(
        "api/v1/org/<str:org_id>/messages/<str:message_id>/read",
        messaging.mark_read,
        name="mark_read",
    ),
    path(  # might require a room id
        "api/v1/org/<str:org_id>/messages/<str:message_id>/pin",
        messaging.pinned_message,
        name="pin_message",
    ),
    path(  # it is creating a reminder for a message
        "api/v1/org/<str:org_id>/reminder",
        views.create_reminder,
        name="create_reminder",
    ),
    path(  # review needed???
        "api/v1/<str:org_id>/<str:room_id>/filter_messages",
        views.message_filter,
        name="message_filter",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/reply",
        views.send_reply,
        name="reply",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/links",
        booklinks.get_links,
        name="get_links",
    ),
    path(
        "api/v1/org/<str:org_id>/messages/<str:message_id>/link",
        booklinks.copy_message_link,
        name="copy_message_link",
    ),
    path(  # review needed
        "getmessage/<str:room_id>/<str:message_id>",
        booklinks.read_message_link,
        name="read_message_link",
    ),
    path(
        "api/v1/<str:org_id>/<str:room_id>/<str:message_id>/pinnedmessage/",
        booklinks.read_message_link,
        name="read_pinned_message",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/new-bookmark",
        booklinks.save_bookmark,
        name="create_bookmark",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/bookmarks",
        booklinks.retrieve_bookmarks,
        name="get_bookmarks",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/bookmark",
        booklinks.delete_bookmark,
        name="delete_bookmark",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/reactions",
        reactions.Emoji.as_view(),
        name="message_reactions",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads/<str:thread_message_id>/reactions",
        reactions.ThreadEmoji.as_view(),
        name="edit_message",
    ),
    path(
        "api/v1/org/<str:org_id>/message/<str:message_id>",
        messaging.MessageDetailsView.as_view(),
        name="thread_message_reaction",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads/<str:thread_message_id>/read_status",
        threads.update_thread_read_status,
        name="update_thread_read_status",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads/<str:thread_message_id>/channel_message",
        threads.send_thread_message_to_channel,
        name="send_thread_messsage_to_channel",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads/<str:thread_message_id>/link",
        threads.copy_thread_message_link,
        name="copy_thread_messsage_link",
    ),
    path(
        "thread_message/<str:org_id>/<str:room_id>/<str:message_id>/<str:thread_message_id>",
        threads.read_thread_message_link,
        name="read_thread_messsage_link",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads/<str:thread_message_id>/pinned",
        threads.pinned_thread_message,
        name="pinned_thread_messsage",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads",
        threads.ThreadListView.as_view(),
        name="thread_messsage_create_get",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads/<str:thread_message_id>",
        threads.ThreadDetailView.as_view(),
        name="thread_messsage_update_delete",
    ),
    path(
        "api/v1/org/<str:org_id>/users/<str:member_id>/threads",
        threads.get_all_threads,
        name="get_all_threads",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messagemedia",
        media.SendFile.as_view(),
        name="media_files",
    ),
    path(
        "api/v1/org/<str:org_id>/members",
        members.organization_members,
        name="organization_members",
    ),
    path(
        "api/v1/org/<str:org_id>/members/<str:member_id>/profile",
        members.user_profile,
        name="user_profile",
    ),
    path(
        "api/v1/org/<str:org_id>/messages",
        messaging.all_messages,
        name="all_messages",
    ),
    path("api/v1/sync", sync.sync_notifier, name="sync_notifier"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
