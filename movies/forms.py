from django.contrib.auth import get_user_model
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import (DateField, ModelChoiceField, ModelForm,
                          SelectDateWidget, ValidationError)

from .models import Movie, Rentals


class MovieFrom(ModelForm):
    
    class Meta:
        model = Movie
        fields = ('name', 'synopsis', 'copies')
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        
        
class LendsForm(ModelForm):
    
    user_id = ModelChoiceField(queryset=get_user_model().objects.all())
    movie_id = ModelChoiceField(queryset=Movie.objects.all())
    max_date = DateField(widget=SelectDateWidget(empty_label="Nothing"))
    
    class Meta:
        model = Rentals
        fields = ('user_id', 'movie_id', 'copies', 'max_date')
        
    def clean(self):
        data = self.cleaned_data
        movie = Movie.objects.get(movie_id=data['movie_id'].movie_id)
    
        result = movie.copies - data['copies']
        
        if result < 0:
            raise ValidationError(
                'There are not sufficient copies, you requested %i but there are only %i' 
                % (data['copies'], movie.copies))
        
        movie.copies = result
        movie.save()
        return super().clean()

