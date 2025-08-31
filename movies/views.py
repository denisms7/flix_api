from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from .serializers import MovieSerializer
from app.permissions import GlobalPermission

class MovieAddList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset  = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetEditDel(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer