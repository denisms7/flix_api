from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Genre
from genres.serializers import GenreSerializer
from app.permissions import GlobalPermission

class GenreAddList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetEditDel(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
