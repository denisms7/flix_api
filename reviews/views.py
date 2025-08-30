from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializers


class ReviewAddList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset  = Review.objects.all()
    serializer_class = ReviewSerializers


class ReviewDetEditDel(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

