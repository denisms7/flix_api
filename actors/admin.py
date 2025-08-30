from django.contrib import admin
from actors.models import Actor


@admin.register(Actor)
class ActorActor(admin.ModelAdmin):
    list_display = ('id', 'name', 'nationality',)
