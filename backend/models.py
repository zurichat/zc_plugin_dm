from django.db import models
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
