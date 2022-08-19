from rest_framework.serializers import ModelSerializer

from api import proxy


class MovieSerializer(ModelSerializer):
    
    class Meta:
        model = proxy.get_model('movies', 'Movie')
        fields = ('movie_id', 'name', 'synopsis', 'copies', 'created_at')
        read_only_fields = ('movie_id', 'created_at',)
