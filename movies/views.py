from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import LendsForm, MovieFrom
from .models import Movie, Rentals


class MoviesList(ListView):
    model = Movie
    template_name = 'movies/list.html'
    

class MovieCreator(CreateView):
    model = Movie
    form_class = MovieFrom
    template_name = 'movies/new_movie.html' 
    success_url = reverse_lazy('movies:home')
    

class LendCreator(CreateView):
    model = Rentals
    form_class = LendsForm
    template_name = 'movies/new_lend.html' 
    success_url = reverse_lazy('movies:lends')
    

class LendsList(ListView):
    
    model = Rentals
    template_name = 'movies/lends.html'
    
    