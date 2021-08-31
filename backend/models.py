from django.db import models
from django.contrib.auth.models import User

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
        