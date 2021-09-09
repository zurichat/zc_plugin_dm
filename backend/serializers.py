from django.utils import timezone
from datetime import datetime
from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    sender_id = serializers.CharField(max_length=128)
    receiver_id = serializers.CharField(max_length=128)
    room_id = serializers.CharField(max_length=128)
    message = serializers.CharField()
    created_at = serializers.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.message)
    

class RoomSerializer:
    def __init__(self, org_id, id1, id2, name1=None, name2=None):
        self.org_id = org_id
        self.id1 = id1
        self.id2 = id2
        self.name1 = name1
        self.name2 = name2
        self.created = datetime.now()
    
    def serialize(self):
        return {
            "org_id": self.org_id,
            "room_user_ids": (self.id1, self.id2),
            "room_usernames": (self.name1, self.name2),
            "created_at": self.created
        }