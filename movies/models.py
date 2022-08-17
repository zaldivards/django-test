from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver

# Create your models here.


class Movie(models.Model):
    
    movie_id = models.AutoField(primary_key=True)
    loans = models.ManyToManyField(get_user_model(), through='Rentals',
                                   related_name='borrowings')
    name = models.CharField(max_length=1000, null=False)
    synopsis = models.CharField(max_length=2500, null=False)
    copies = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Rentals(models.Model):
    
    rental_id = models.AutoField(primary_key=True)
    
    movie_id = models.ForeignKey(Movie, null=False, db_column='movie_id',
                                 on_delete=models.CASCADE)
    
    user_id = models.ForeignKey(get_user_model(), null=False, db_column='user_id',
                                 on_delete=models.CASCADE)
    
    copies = models.IntegerField(null=True, default=1)
    
    max_date = models.DateField(null=False)
    
    