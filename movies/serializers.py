from rest_framework import serializers
from django.db.models import Avg
from .models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieSerializerDetail(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "genres",
            "actors",
            "release_date",
            "rate",
            "resume",
        ]

    def get_rate(self, obj):
        """Retorna a média arredondada das estrelas de reviews."""
        rate = obj.reviews.aggregate(avg=Avg("stars"))["avg"]
        if rate is not None:
            return round(rate, 1)
        return None


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

    # validacao de dados  do campo release_date
    def validate_release_date(self, value):
        if value.year < 1888:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1888.')
        return value
