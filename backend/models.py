from django.db import models
from django.contrib.auth import get_user_model



class book_mark(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    link = models.CharField(max_length=900)
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

    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="sender_rooms")
    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="receiver_rooms")
    seen = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def delete(self) -> None:
        self.deleted = True
        self.save()

    def __str__(self) -> str:
        return f"sender:{self.sender}\treceiver:{self.receiver}\tseen:{self.seen}\tdeleted:{self.deleted}"


User = get_user_model()
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
class Message(models.Model):
    sender_id = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name="sent")
    receiver_id = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name="received")
    message = models.TextField()
    meta = models.JSONField()
    deleted_user_id = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.sender_id.username} sent '{self.message} ' to {self.receiver_id} "
    
