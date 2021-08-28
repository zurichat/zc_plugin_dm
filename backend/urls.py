from . import views
from django.urls import path 

app_name = 'backend'

urlpatterns = [
    path('', views.index, name='index')
]
