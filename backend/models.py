from django.db import models
from django.contrib.auth.models import User
"""
    Main entities
    1.User
            all users can be senders or recievers 
    2.Message
    

"""
# user model==> one to relationship with the Default django users
# first scenarion sender-->message--> recipient
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # any required filed here
    
    # def __str__(self):
    #     return self.User.username
    
    
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
        # ordering = ("timestamp")
        
class Delivery(models.Model):
    reciver = models.ForeignKey(User, on_delete=models.CASCADE)
    # recipient_group = 


class Media(models.Model):
    MessagesId=models.ForeignKey(Messages,on_delete=models.CASCADE)
    # saving file with date
    media = models.FileField(upload_to='media/%Y/%m/%d', max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class  Meta:
        ordering = ('timestamp',)
        