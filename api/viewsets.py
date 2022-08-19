from rest_framework.viewsets import ModelViewSet

from api import proxy

from .serializers import MovieSerializer


class MovieViewSet(ModelViewSet):
    
    queryset = proxy.get_model('movies', 'Movie').objects.all()
    serializer_class = MovieSerializer
    
