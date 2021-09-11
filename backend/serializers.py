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
    ''' OwnerId    primitive.ObjectID   `json:"ownerid,omitempty" bson:"ownerid,omitempty"` automatic
        string               
        RoomType   string                //inbox, group, channel
        Members    []primitive.ObjectID 
        CreatedAt  string               
        Archived   string              
        ArchivedBy primitive.ObjectID   
        ArchiveAt  string               
        Private    string                // {true, false} inbox, group is private by default
        '''
    RoomName = serializers.CharField(max_length = 100)
    RoomType = serializers.CharField(max_length = 100)
    Members = serializers.ListField(child=serializers.CharField(max_length=128),
                                         allow_empty=False)
    CreatedAt =serializers.DateTimeField(default=timezone.now)
    Archived = serializers.BooleanField(default=False)
    ArchivedBy = serializers.ListField(default=None)
    Private = serializers.CharField(default=True)
    # org_id = serializers.CharField(max_length=128) removed due to repetition
    
    def __str__(self):
        return str()
