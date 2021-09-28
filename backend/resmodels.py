from rest_framework import serializers


class RoomInfoResponse(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    org_id = serializers.CharField(read_only=True)
    room_user_ids = serializers.ListField(child=serializers.CharField(read_only=True))
    created_at = serializers.DateTimeField(read_only=True)
    description = serializers.CharField(read_only=True)


class MessageResponse(serializers.Serializer):
    status = serializers.CharField(read_only=True)
    event = serializers.ReadOnlyField()
    message_id = serializers.ReadOnlyField()
    thread = serializers.BooleanField()
    data = serializers.DictField(child=serializers.CharField(), read_only=True)
    created_at = serializers.DateTimeField(read_only=True)


class ThreadResponse(serializers.Serializer):
    status = serializers.CharField(read_only=True)
    message_id = serializers.ReadOnlyField()
    thread_id = serializers.ReadOnlyField()
    thread = serializers.BooleanField()
    data = serializers.DictField(child=serializers.CharField(), read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

class CreateRoomResponse(serializers.Serializer):
    room_id = serializers.ReadOnlyField()

class MessageLinkResponse(serializers.Serializer):
    room_id = serializers.ReadOnlyField()
    message_id = serializers.ReadOnlyField()
    link = serializers.URLField(read_only=True)

class UserRoomsResponse(serializers.Serializer):
    pass

class UserProfileResponse(serializers.Serializer):
    name = serializers.ReadOnlyField()
    display_name = serializers.ReadOnlyField()
    bio = serializers.ReadOnlyField()
    pronouns = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    phone = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()

class BookmarkResponse(serializers.Serializer):
    link = serializers.URLField(read_only=True)
    name = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField()

class PinMessageResponse(serializers.Serializer):
    room_id = serializers.CharField(read_only=True)
    bookmarks = serializers.ListField(read_only=True)
    created_at = serializers.DateTimeField()
    org_id = serializers.CharField(read_only=True)
    pinned = serializers.ListField(read_only=True)
    room_user_ids = serializers.ListField(read_only=True)

class UnpinMessageResponse(serializers.Serializer):
    pinned = serializers.ListField(read_only=True)

class FilterMessageResponse(serializers.Serializer):
    message_id = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField()
    media = serializers.ListField(read_only=True)
    message = serializers.CharField(read_only=True)
    pinned = serializers.BooleanField()
    reactions = serializers.ListField(read_only=True)
    read = serializers.BooleanField()
    room_id = serializers.CharField(read_only=True)
    saved_by = serializers.ListField(read_only=True)
    sender_id = serializers.CharField(read_only=True)
    threads = serializers.ListField(read_only=True)

class GetLinksResponse(serializers.Serializer):
    links = serializers.ReadOnlyField()
    timestamp = serializers.ReadOnlyField()
    room_id = serializers.ReadOnlyField()