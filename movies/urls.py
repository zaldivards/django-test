from django.urls import path

from .views import LendCreator, LendsList, MovieCreator, MoviesList

urlpatterns = [
    path('', MoviesList.as_view(), name='home'),
    path('lends', LendsList.as_view(), name='lends'),
    path('add-movie', MovieCreator.as_view(), name='movies_creation'),
    path('add-lend', LendCreator.as_view(), name='lends_creation')
    
]
