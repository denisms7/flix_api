from rest_framework import generics
from .models import Actor
from  .serializer import ActorSerializer

class ActorsAddList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class =  ActorSerializer


class ActorsDetEditDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    