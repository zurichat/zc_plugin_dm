from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import book_mark, Message

# User serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

# Bookmark serializer


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = book_mark
        fields = '__all__'


"""
    serializer that takes in messages model to facilitate 
    GET,PUT and Update
"""


class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = "__all__"
    

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id',
                  'sender_id',
                  'receiver_id',
                  'message',
                  'created_at',
                  'last_updated')
