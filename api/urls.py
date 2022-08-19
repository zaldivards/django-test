from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import MovieViewSet

movies_router = DefaultRouter(trailing_slash=False)

movies_router.register('movies', MovieViewSet, basename='movies')

urlpatterns = [
    path('', include(movies_router.urls))
]

print(movies_router.urls)
