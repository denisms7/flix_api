from rest_framework import generics
from .models import Actor
from  .serializer import ActorSerializer
from rest_framework.permissions import IsAuthenticated


class ActorsAddList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class =  ActorSerializer


class ActorsDetEditDel(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    