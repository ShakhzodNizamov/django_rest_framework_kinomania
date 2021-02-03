from rest_framework import serializers

from .models import Movie


class MovieListSerializer(serializers.ModelSerializer):
    """Список Фильмов"""

    class Meta:
        model = Movie
        fields = ('id', 'title', 'tagline', 'category')


class MovieDetailSerializer(serializers.ModelSerializer):
    """Детальное описание Фильма"""
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    directors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Movie
        exclude = ('draft',)
