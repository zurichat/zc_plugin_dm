from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class book_mark(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    link = models.CharField(max_length=900)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.user
