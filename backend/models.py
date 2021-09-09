from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# acting for user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Media(models.Model):
    #MessagesId = models.ForeignKey(Message, on_delete=models.CASCADE)
    # saving file with date
    media = models.FileField(upload_to='media/%Y/%m/%d', max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)


class Message(models.Model):
    """
The message model simulates the Messages being sent by users to one another.
In The message model we have the following fields:
        -   sender_id: This is senders id and references the user model via a foreignkey
        -   receiver_id: This is receivers id and references the user model via a foreignkey
        -   deleted_user_id: This is users id that deletes a particular message and references the user model via a foreignkey
        -   message: This is the message being sent to each other.
        -   meta: This is a Json Object which contains more detailed info about the message being sent
        -   created_at: The date at which the message was created
        -   last_updated: The date at which the message was last updated
"""
   
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.user


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

    sender = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="sender_rooms")
    receiver = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="receiver_rooms")
    seen = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def delete(self) -> None:
        self.deleted = True
        self.save()

    def __str__(self) -> str:
        return f"sender:{self.sender}\treceiver:{self.receiver}\tseen:{self.seen}\tdeleted:{self.deleted}"
