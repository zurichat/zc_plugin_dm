from django.contrib import admin
from .models import Profile, Media, Messages
# Register your models here.
admin.site.register(Media)
admin.site.register(Messages)
admin.site.register(Profile)
