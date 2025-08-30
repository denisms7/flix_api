from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Genre
from genres.serializers import GenereSirealizer

class GenreAddList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenereSirealizer

class GenreDetEditDel(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenereSirealizer
