from django.contrib import admin
from movies.models import Movie


@admin.register(Movie)
class MovieActor(admin.ModelAdmin):
    list_display = ('title', 'release_date',)
