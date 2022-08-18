from datetime import date

from django.contrib.auth import get_user_model
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import (DateField, ModelChoiceField, ModelForm,
                          SelectDateWidget, ValidationError)
from django.forms.utils import ErrorList

from .models import Movie, Rentals


def validate_max_date(previous_date: date, new_date: date):
    if new_date < previous_date:
        raise ValidationError(
            "The minimum date to return a movie it's"
            "today or the previously set date"
        )


class MovieFrom(ModelForm):

    class Meta:
        model = Movie
        fields = ('name', 'synopsis', 'copies', 'rented_copies')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data
        if self.request == 'PUT':
            existent_rentals = (Rentals.objects
                                .get_rented_copies(
                                    self.instance.movie_id
                                )['rented_copies']
                                )

            existent_rentals = (existent_rentals
                                if existent_rentals is not None
                                else 0)

            if data['copies'] < existent_rentals:
                raise ValidationError(
                    "There must be sufficient copies for the existing rentals."
                    "\nExisting rentals: %i" % existent_rentals)
        return super().clean()


class LendsForm(ModelForm):

    user_id = ModelChoiceField(queryset=get_user_model().objects.all())
    movie_id = ModelChoiceField(queryset=Movie.objects.all())
    max_date = DateField(widget=SelectDateWidget(empty_label="Nothing"))

    class Meta:
        model = Rentals
        fields = ('user_id', 'movie_id', 'copies', 'max_date')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data
        movie = Movie.objects.get(movie_id=data['movie_id'].movie_id)

        copies = movie.rented_copies + data['copies']

        copies_left = movie.copies - movie.rented_copies

        if self.request == 'PUT':

            validate_max_date(self.instance.max_date, data['max_date'])

            if self.instance.copies > data['copies']:
                new_copies = (self.instance.copies - data['copies'])
                copies = movie.rented_copies + new_copies
                movie.rented_copies -= new_copies
            else:
                new_copies = (data['copies'] - self.instance.copies)
                copies = movie.rented_copies + new_copies
                movie.rented_copies += new_copies
        else:
            validate_max_date(date.today(), data['max_date'])
            movie.rented_copies += data['copies']

        if copies > movie.copies:
            raise ValidationError(
                'There are not sufficient copies, '
                'you requested %i but there are only %i'
                % (data['copies'], copies_left))

        movie.save()
        return super().clean()
