from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer


class MovieAddList(generics.ListCreateAPIView):
    queryset  = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetEditDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer