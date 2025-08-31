from rest_framework import generics
from .models import Actor
from  .serializer import ActorSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermission

class ActorsAddList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Actor.objects.all()
    serializer_class =  ActorSerializer


class ActorsDetEditDel(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    