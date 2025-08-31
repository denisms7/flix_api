from rest_framework import serializers
from django.db.models import Avg
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    # Delve o rate apenas em modo get get_rate
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate,1)
        return None

    # validacao de dados  do campo release_date
    def validate_release_date(self, value):
        if value.year < 1888:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1888.')
        return value
    