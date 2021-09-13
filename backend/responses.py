from rest_framework import serializers


class RoomInfoResponse(serializers.Serializer):
    _id = serializers.ReadOnlyField()
    org_id = serializers.CharField(read_only=True)
    room_user_ids = serializers.ListField(child=serializers.CharField(read_only=True))
    created_at = serializers.DateTimeField(read_only=True)
    description = serializers.CharField(read_only=True)


class MessageResponse(serializers.Serializer):
    pass


class CreateRoomResponse(serializers.Serializer):
    pass


class UserRoomsResponse(serializers.Serializer):
    pass