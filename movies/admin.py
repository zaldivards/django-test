from django.contrib import admin

from .models import Movie, Rentals

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'synopsis', 'copies', 'created_at')


class RentalsAdmin(admin.ModelAdmin):
    list_display = ('rental_id', 'movie', 'user_name', 'copies', 'max_date')

    def user_name(self, obj, *args, **kwargs):
        return str(obj.user_id)

    def movie(self, obj, *args, **kwargs):
        return obj.movie_id.name
