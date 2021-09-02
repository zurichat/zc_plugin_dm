from .models import book_mark
from rest_framework import fields, serializers


class BookmarkSerializer(serializers.Serializer):
    class Meta:
        model = book_mark
        fields = '__all__'