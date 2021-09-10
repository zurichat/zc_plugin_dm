from django.utils import timezone

from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    sender_id = serializers.CharField(max_length=128)
    receiver_id = serializers.CharField(max_length=128)
    room_id = serializers.CharField(max_length=128)
    message = serializers.CharField()
    created_at = serializers.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.message)


class RoomSerializer(serializers.Serializer):
    org_id = serializers.CharField(max_length=128)
    room_user_ids = serializers.ListField(child=serializers.CharField(max_length=128),
                                           allow_empty=False)
    created_at = serializers.DateTimeField(default=timezone.now)

    def __str__(self):
        return str()
