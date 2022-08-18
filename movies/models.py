from django.contrib.auth import get_user_model
from django.db import models, transaction

# Create your models here.


class Movie(models.Model):
    
    movie_id = models.AutoField(primary_key=True)
    loans = models.ManyToManyField(get_user_model(), through='Rentals',
                                   related_name='borrowings')
    name = models.CharField(max_length=1000, null=False)
    synopsis = models.CharField(max_length=2500, null=False)
    copies = models.IntegerField(null=False)
    rented_copies = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class RentalsManager(models.Manager):
    
    @transaction.atomic()
    def remove_lend(self, id_: int):
        try:
            obj = self.get(rental_id=id_)
            copies = obj.copies
            movie_id = obj.movie_id
            obj.delete()
        except Exception as e:
            print(e)
            raise e
        else:
            try:
                movie: Movie = Movie.objects.get(pk=movie_id.movie_id)
                movie.rented_copies -= copies
                movie.save()
            except Exception as e:
                raise e
            
    
    def get_rented_copies(self, movie_id) -> int:
        try:
            return self.filter(movie_id_id=movie_id).aggregate(rented_copies=models.Sum('copies'))
        except Exception as e:
            print(e)
            raise

class Rentals(models.Model):
    
    rental_id = models.AutoField(primary_key=True)
    
    movie_id = models.ForeignKey(Movie, null=False, db_column='movie_id',
                                 on_delete=models.CASCADE)
    
    user_id = models.ForeignKey(get_user_model(), null=False, db_column='user_id',
                                 on_delete=models.CASCADE)
    
    copies = models.IntegerField(null=True, default=1)
    
    max_date = models.DateField(null=False)
    
    
    objects = RentalsManager()
