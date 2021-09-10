from . import views
from django.urls import path

app_name = 'backend'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/info', views.info, name='plugin_info'),
    path('api/v1/sidebar', views.side_bar, name='sidebar'),
    path('api/v1/send-data', views.send_message, name="send_data"),
    path('api/v1/createroom', views.create_room, name='createroom'),
]
