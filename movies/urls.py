from django.urls import path

from .views import (LendCreator, LendEdit, LendsList, MovieCreator, MovieEdit,
                    MoviesList, movieRemover, rentalRemover)

urlpatterns = [
    path('', MoviesList.as_view(), name='home'),
    path('new', MovieCreator.as_view(), name='movies_creation'),
    path('delete/<int:id_>', movieRemover, name='movie_delete'),
    path('edit/<int:pk>', MovieEdit.as_view(), name='movie_edit'),
    path('lends', LendsList.as_view(), name='lends'),
    path('lends/new', LendCreator.as_view(), name='lends_creation'),
    path('remove-lend/<int:id_>', rentalRemover, name='rental_delete'),
    path('lends/edit/<int:pk>', LendEdit.as_view(), name='rental_edit')
    
]
