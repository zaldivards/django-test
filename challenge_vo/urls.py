"""challenge_vo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

...

schema_view = get_schema_view(
   openapi.Info(
      title="Movie rentals API",
      default_version='v1',
      description="Open api test",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="herrerachristian@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('movies/', include(('movies.urls', 'movies'), namespace="movies")),
    path('api/v1/', include('api.urls')),
    path('admin/', admin.site.urls, name='admin')
]


admin.site.site_header = "Welcome to the user admin portal"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "User admin portal"
admin.site.site_url='/movies/'
