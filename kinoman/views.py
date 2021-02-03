from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer


class MovieListView(APIView):
    """Вывод списка фильмов"""

    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    """Вывод детальное описание фильма"""

    def get(self, request, primary_key):
        movie = Movie.objects.get(id=primary_key, draft=False)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
