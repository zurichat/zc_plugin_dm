from . import views
from .testingapi import Test

# from .views import EditMessage
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("api/v1/ping", views.PING, name="ping"),
    path("api/v1/info", views.info, name="plugin_info"),
    path("api/v1/sidebar", views.side_bar, name="sidebar"),
    path(
        "api/v1/org/<str:org_id>/members/<str:member_id>/messages/search",
        views.search_DM,
        name="search DM",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages",
        views.message_create_get,
        name="create_get_message",
    ),
    # path(
    #     "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads/<str:message_uuid>",
    #     views.update_thread_message,
    #     name="update_thread_message",
    # ),
    path(
        "api/v1/org/<str:org_id>/users/<str:member_id>/room",
        views.create_room,
        name="create_room",
    ),
    path(
        "api/v1/org/<str:org_id>/updatemessage/<str:message_id>/room/<str:room_id>",
        views.edit_message,
        name="updateroom",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/info",
        views.room_info,
        name="room_info",
    ),
    path(
        "api/v1/org/<str:org_id>/users/<str:user_id>/rooms",
        views.user_rooms,
        name="get_user_rooms",
    ),
    path(  # it is creating a reminder for a message
        "api/v1/org/<str:org_id>/reminder",
        views.create_reminder,
        name="create_reminder",
    ),
    path(
        "api/v1/org/<str:org_id>/messages/<str:message_id>/link",
        views.copy_message_link,
        name="copy_message_link",
    ),
    path(  # review needed
        "getmessage/<str:room_id>/<str:message_id>",
        views.read_message_link,
        name="read_message_link",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/links",
        views.get_links,
        name="get_links",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/new-bookmark",
        views.save_bookmark,
        name="create_bookmark",
    ),
    path(
        "api/v1/org/<str:org_id>/members",
        views.organization_members,
        name="organization_members",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/bookmarks",
        views.retrieve_bookmarks,
        name="get_bookmarks",
    ),
    path(
        "api/v1/org/<str:org_id>/messages/<str:message_id>/read",
        views.mark_read,
        name="mark_read",
    ),
    path(  # might require a room id
        "api/v1/org/<str:org_id>/messages/<str:message_id>/pin",
        views.pinned_message,
        name="pin_message",
    ),
    # path( #???
    #     "api/v1/<str:org_id>/messages/<str:message_id>/unpin",
    #     views.delete_pinned_message,
    #     name="unpin_message",
    # ),
    path(  # review needed
        "api/v1/<str:org_id>/<str:room_id>/<str:message_id>/pinnedmessage/",
        views.read_message_link,
        name="read_pinned_message",
    ),
    path(  # review needed???
        "api/v1/<str:org_id>/<str:room_id>/filter_messages",
        views.message_filter,
        name="message_filter",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/message",
        views.delete_message,
        name="delete_message",
    ),
    path(
        "api/v1/org/<str:org_id>/members/<str:member_id>/profile",
        views.user_profile,
        name="user_profile",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messagemedia",
        views.SendFile.as_view(),
        name="media_files",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/reply",
        views.send_reply,
        name="reply",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/reactions",
        views.Emoji.as_view(),
        name="message_reactions",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/schedule-message",
        views.scheduled_messages,
        name="scheduled_messages",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/bookmark",
        views.delete_bookmark,
        name="delete_bookmark",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads",
        views.ThreadListView.as_view(),
        name="messages_thread_list",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads/<str:thread_message_id>",
        views.ThreadDetailView.as_view(),
        name="messages_thread_detail",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads/<str:thread_message_id>/reactions",
        views.ThreadEmoji.as_view(),
        name="thread_message_reaction",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads/<str:thread_message_id>/reactions/<str:reaction_id>",
        views.delete_thread_emoji_reaction,
        name="delete_thread_message_reaction",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads/<str:thread_message_id>/read_status",
        views.update_thread_read_status,
        name="update_thread_read_status",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads/<str:thread_message_id>/channel_message",
        views.send_thread_message_to_channel,
        name="send_thread_messsage_to_channel",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads/<str:thread_message_id>/link",
        views.copy_thread_message_link,
        name="copy_thread_messsage_link",
    ),
    path(
        "thread_message/<str:org_id>/<str:room_id>/<str:message_id>/<str:thread_message_id>",
        views.read_thread_message_link,
        name="read_thread_messsage_link",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/messages/<str:message_id>/threads/<str:thread_message_id>/pinned",
        views.pinned_thread_message,
        name="pinned_thread_messsage",
    ),
    path(
        "api/v1/org/<str:org_id>/users/<str:member_id>/threads",
        views.get_all_threads,
        name="get_all_threads",
    ),
    path(
        "api/v1/org/<str:org_id>/rooms/<str:room_id>/members/<str:member_id>/star",
        views.star_room,
        name="star_room",
    ),
    path("api/v1/org/<str:org_id>/rooms/<str:room_id>/members/<str:member_id>/close_conversation", 
        views.close_conversation, 
        name="close_conversation"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
