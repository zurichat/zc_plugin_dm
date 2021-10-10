import re

from django.utils import timezone
from datetime import datetime
from rest_framework import serializers


class EmojiSerializer(serializers.Serializer):
    message_id = serializers.CharField(max_length=128)
    sender_id = serializers.CharField(max_length=128)
    data = serializers.CharField(max_length=128)
    category = serializers.CharField(max_length=128)
    aliases = serializers.ListField(
        child=serializers.CharField(max_length=128), required=False, default=[]
    )
    count = serializers.IntegerField()
    created_at = serializers.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.data)


class ReminderSerializer(serializers.Serializer):
    message_id = serializers.CharField(max_length=500)
    current_date = serializers.CharField(max_length=500)
    scheduled_date = serializers.CharField(max_length=500)
    notes = serializers.CharField(required=False,max_length=500, allow_blank=True)
    class Meta: 
        fields = ['__all__']


class ThreadSerializer(serializers.Serializer):
    # """
    # this will server as a serializer to hold threads
    # under a particular message.
    # The threads serializer will be used in the
    # Message serializer
    # """

    message_id = serializers.CharField(max_length=128, required=False)
    sender_id = serializers.CharField(max_length=128, required=False)
    message = serializers.CharField(required=False)
    media = serializers.ListField(
        child=serializers.URLField(), allow_empty=True, required=False, default=[]
    )
    read = serializers.BooleanField(default=False, required=False)
    pinned = serializers.BooleanField(default=False, required=False)
    reactions = serializers.ListField(
        required=False, default=[], child=EmojiSerializer()
    )
    created_at = serializers.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.message)


class MessageSerializer(serializers.Serializer):
    sender_id = serializers.CharField(max_length=128)
    room_id = serializers.CharField(max_length=128)
    message = serializers.CharField()
    media = serializers.ListField(
        child=serializers.URLField(), allow_empty=True, required=False, default=[]
    )
    read = serializers.BooleanField(default=False, required=False)
    pinned = serializers.BooleanField(default=False, required=False)
    saved_by = serializers.ListField(
        child=serializers.CharField(max_length=128), required=False, default=[]
    )
    threads = serializers.ListField(
        required=False, default=[], child=ThreadSerializer()
    )
    replied_message = serializers.ListField(
        required=False, default=[]
    )
    reactions = serializers.ListField(
        required=False, default=[], child=EmojiSerializer()
    )
    created_at = serializers.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.message)

    def update(self, instance, validated_data):
        print(validated_data)
        instance["sender_id"] = validated_data.get(
            "sender_id", instance["sender_id"])
        instance["room_id"] = validated_data.get(
            "room_id", instance["room_id"])
        instance["message"] = validated_data.get(
            "message", instance["message"])

        # instance["created_at"] = validated_data.get('created_at', instance["created_at"] ) read only

        return instance


class RoomSerializer(serializers.Serializer):
    org_id = serializers.CharField(max_length=128, required=True)
    room_member_ids = serializers.ListField(
        child=serializers.CharField(max_length=128), allow_empty=False, required=True
    )
    room_name = serializers.CharField(max_length=128, required=True)
    private = serializers.BooleanField(default=True, read_only=True)
    created_at = serializers.DateTimeField(
        default=timezone.now, read_only=True)

    def __str__(self):
        return str()


class RoomInfoSerializer(serializers.Serializer):
    room_id = serializers.CharField(max_length=128)


class GetMessageSerializer(serializers.Serializer):
    date = serializers.DateField(
        format="%d-%m-%Y", input_formats=["%d-%m-%Y", "iso-8601"], required=False
    )


class UserRoomsSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=128)


class BookmarkSerializer(serializers.Serializer):
    link = serializers.CharField()
    name = serializers.CharField()
    created_at = serializers.DateTimeField(default=timezone.now)

    def validate_link(self, value):
        pattern = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
        if not re.match(pattern, value):
            raise serializers.ValidationError("Invalid link for bookmark")
        return value


class ReadSerializer(serializers.Serializer):
    message_id = serializers.CharField(max_length=128)


class CookieSerializer(serializers.Serializer):
    cookie = serializers.CharField(max_length=150)


class DeleteMessageSerializer(serializers.Serializer):
    message_id = serializers.CharField(max_length=128)


class ScheduleMessageSerializer(serializers.Serializer):
    sender_id = serializers.CharField(max_length=128)
    room_id = serializers.CharField(max_length=128)
    message = serializers.CharField()
    timer = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def validate_timer(self, timer):
        if datetime.now() > timer.replace(tzinfo=None):
            raise serializers.ValidationError("Date cannot be in the past.")
        return timer
