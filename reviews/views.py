from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializers


class ReviewAddList(generics.ListCreateAPIView):
    queryset  = Review.objects.all()
    serializer_class = ReviewSerializers


class ReviewDetEditDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

