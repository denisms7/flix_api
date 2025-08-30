from rest_framework import generics
from .models import Genre
from genres.serializers import GenereSirealizer

class GenreAddList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenereSirealizer

class GenreDetEditDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenereSirealizer
