from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, ListView, UpdateView

from .forms import LendsForm, MovieFrom
from .mixins import ManageErrorResponseMixin, MockRequestMixin
from .models import Movie, Rentals

EDIT_MESSAGE = 'Successfully updated!'
SAVE_MESSAGE = 'Successfully created!'
ERROR_MESSAGE = 'Something went wrong, contact the administrator'


class MoviesList(ListView):
    model = Movie
    template_name = 'movies/list.html'


class MovieCreator(SuccessMessageMixin, MockRequestMixin, ManageErrorResponseMixin, CreateView):
    model = Movie
    form_class = MovieFrom
    template_name = 'movies/new_movie.html'
    success_url = reverse_lazy('movies:home')
    success_message = SAVE_MESSAGE
    error_message = ERROR_MESSAGE
    form_type = 'POST'


class MovieEdit(SuccessMessageMixin, MockRequestMixin, ManageErrorResponseMixin, UpdateView):
    model = Movie
    form_class = MovieFrom
    template_name = 'movies/edit_movie.html'
    success_url = reverse_lazy('movies:home')
    success_message = EDIT_MESSAGE
    error_message = ERROR_MESSAGE
    form_type = 'PUT'


@require_http_methods(['DELETE'])
def movieRemover(request, id_):
    try:
        Movie.objects.get(movie_id=id_).delete()
    except Exception as e:
        return JsonResponse({'message': 'Error :' + str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Success'}, status=204)


class LendCreator(SuccessMessageMixin, MockRequestMixin, ManageErrorResponseMixin, CreateView):
    model = Rentals
    form_class = LendsForm
    template_name = 'movies/new_lend.html'
    success_url = reverse_lazy('movies:lends')
    success_message = SAVE_MESSAGE
    error_message = ERROR_MESSAGE
    form_type = 'POST'


class LendsList(ListView):

    model = Rentals
    template_name = 'movies/lends.html'


class LendEdit(SuccessMessageMixin, MockRequestMixin, ManageErrorResponseMixin, UpdateView):
    model = Rentals
    template_name = 'movies/edit_lend.html'
    form_class = LendsForm
    success_url = reverse_lazy('movies:lends')
    success_message = EDIT_MESSAGE
    error_message = ERROR_MESSAGE
    form_type = 'PUT'


@require_http_methods(['DELETE'])
def rentalRemover(request, id_):
    try:
        Rentals.objects.remove_lend(id_)
    except Exception as e:
        return JsonResponse({'message': 'Error: ' + str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Success'}, status=204)
