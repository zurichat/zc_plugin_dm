from rest_framework import serializers


class RoomInfoResponse(serializers.Serializer):
    _id = serializers.ReadOnlyField()
    org_id = serializers.CharField(read_only=True)
    room_user_ids = serializers.ListField(child=serializers.CharField(read_only=True))
    created_at = serializers.DateTimeField(read_only=True)
    description = serializers.CharField(read_only=True)


class MessageResponse(serializers.Serializer):
    status = serializers.CharField(read_only=True)
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