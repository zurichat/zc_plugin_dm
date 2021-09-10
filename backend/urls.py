from . import views
from django.urls import path

app_name = 'backend'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/info', views.info, name='plugin_info'),
    path('api/v1/sidebar', views.side_bar, name='sidebar'),
    path('api/v1/save_message', views.save_message, name="save_message"),
    path('api/v1/createroom', views.create_room, name='createroom'),
	
	
    # test endpoint
    path('test/verify_user_auth', views.test_verify_user_auth, name="test_verify_user_auth"),
]
