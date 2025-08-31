from rest_framework import generics, views, status, response
from django.db.models import Count, Avg
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from reviews.models import Review
from .serializers import MovieSerializer, MovieSerializerDetail
from app.permissions import GlobalPermission
from django.utils import timezone


class MovieAddList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieSerializerDetail
        return MovieSerializer


class MovieDetEditDel(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
        date_time = timezone.localtime(timezone.now()).isoformat()

        return response.Response(
            data={
                'date_time': date_time,
                'total_movies': total_movies,
                'movies_by_genre': movies_by_genre,
                'total_reviews': total_reviews,
                'average_stars': round(average_stars, 1) if average_stars is not None else 0,
            },
            status=status.HTTP_200_OK
        )
