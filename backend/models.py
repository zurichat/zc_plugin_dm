from django.db import models
from django.contrib.auth.models import User
# this is optional, I used this for enabling me create relationship with the messages and file media
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    
class Messages(models.Model):
    message=models.CharField(max_length=1200)
    file=models.FileField(upload_to=None, max_length=100)
    sender = models.ForeignKey(Profile,on_delete=models.CASCADE)
    reciever = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.message
    
    class  Meta:
        ordering = ('timestamp',)
        
        

class Media(models.Model):
    MessagesId=models.ForeignKey(Messages,on_delete=models.CASCADE)
    # saving file with date
    media = models.FileField(upload_to='media/%Y/%m/%d', max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class  Meta:
        ordering = ('timestamp',)
        
from django.contrib.auth import get_user_model


class Room(models.Model):
    """
    The idea here is that a room is a single hub that holds messages between two parties.

    ### Fields
    - `sender` : `User` ; 1st party in a dm room. should be the initiator of the conversation
    - `receiver` : `User` ; 2nd party in a dm room. should be the initial recipient in a conversation
    - `seen`: `boolean` : `default: False` ; flag that indicates whether a room has an unread message.
    - `deleted` : `boolean` : `default: False` ; flag for deleted rooms.

    ### Methods
    - `delete` : `None` ; overrides `Model.delete`. sets the deleted attribute to True.

    ### Differences from the given schema
    - removed the `message` field from here. I believe the room-message relationship should be created
    the message side as a foreignkey where the room is the 1-side and the message is the many-side.
    """

    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="sender_rooms")
    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="receiver_rooms")
    seen = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def delete(self) -> None:
        self.deleted = True
        self.save()

    def __str__(self) -> str:
        return f"sender:{self.sender}\treceiver:{self.receiver}\tseen:{self.seen}\tdeleted:{self.deleted}"
