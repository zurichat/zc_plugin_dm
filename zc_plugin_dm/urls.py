from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Zuri Chat Direct Messaging Plugin API",
      default_version='v1',
      description="Compiled By Team Orpheus HNGi8",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dm_plugin@zuri.chat"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   #validators=["ssv"],
)


#app urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
]


#documentation urls
urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   url(r'^docs/v1/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
