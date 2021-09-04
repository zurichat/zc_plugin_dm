from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import book_mark

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
