from django.utils import timezone
from datetime import datetime
from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    sender_id = serializers.CharField(max_length=128)
    room_id = serializers.CharField(max_length=128)
    message = serializers.CharField(max_length=128)
    # media = serializers.ListField(child=serializers.URLField(), allow_empty=True)
    created_at = serializers.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.message)
    
    def update(self, instance, validated_data):
        print(validated_data)
        instance["sender_id"] = validated_data.get('sender_id', instance["sender_id"])
        instance["room_id"] = validated_data.get('room_id', instance["room_id"])
        instance["message"] = validated_data.get('message', instance["message"])
        
        # instance["created_at"] = validated_data.get('created_at', instance["created_at"] ) read only
        
        return instance
    


class RoomSerializer(serializers.Serializer):
    org_id = serializers.CharField(max_length=128)
    room_user_ids = serializers.ListField(child=serializers.CharField(max_length=128),
                                           allow_empty=False)
    created_at = serializers.DateTimeField(default=timezone.now)

    def __str__(self):
        return str()

class RoomInfoSerializer(serializers.Serializer):
    room_id = serializers.CharField(max_length=128)

    def __str__(self):
        return str(self.room_id)