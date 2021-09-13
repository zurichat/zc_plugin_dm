from django.utils import timezone
from datetime import datetime
from rest_framework import serializers

class ThreadSerializer(serializers.Serializer):
    """
    this will server as a serializer to hold threads 
    under a particular message.
    The threads serializer will be used in the
    Message serializer
    """
    message_id = serializers.CharField(max_length=128)
    sender_id = serializers.CharField(max_length=128)
    message = serializers.CharField()
    media = serializers.ListField(child=serializers.URLField(), allow_empty=True, required=False, default=[])
    created_at = serializers.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.message)

class MessageSerializer(serializers.Serializer):
    sender_id = serializers.CharField(max_length=128)
    room_id = serializers.CharField(max_length=128)
    message = serializers.CharField()
    media = serializers.ListField(child=serializers.URLField(), allow_empty=True, required=False, default=[])
    read = serializers.BooleanField(default=False, required=False)
    pinned = serializers.BooleanField(default=False, required=False)
    saved_by = serializers.ListField(child=serializers.CharField(max_length=128), required=False, default=[])
    threads = serializers.ListField(required=False, default=[], child=ThreadSerializer())
    created_at = serializers.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.message)


class RoomSerializer(serializers.Serializer):
    org_id = serializers.CharField(max_length=128, required=True)
    room_user_ids = serializers.ListField(child=serializers.CharField(max_length=128),
                                           allow_empty=False, required=True)
    created_at = serializers.DateTimeField(default=timezone.now, read_only=True)

    def __str__(self):
        return str()

