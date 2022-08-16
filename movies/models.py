from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Movie(models.Model):
    
    movie_id = models.AutoField(primary_key=True)
    rentals = models.ManyToManyField(get_user_model(), through='Rentals')
    name = models.CharField(max_length=1000, null=False)
    synopsis = models.CharField(max_length=2500, null=False)
    copies = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)



class Rentals(models.Model):
    
    rental_id = models.AutoField(primary_key=True)
    movie_id = models.ForeignKey(Movie, null=False, unique=True, 
                                 on_delete=models.CASCADE)
    
    movie_id = models.ForeignKey(get_user_model(), null=False, unique=True,
                                 on_delete=models.CASCADE)
    
    copies = models.IntegerField(null=True, default=1)
    
    max_date = models.DateField(null=False)
    
    
    
    