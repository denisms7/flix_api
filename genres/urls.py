from django.urls import path
from .views import GenreAddList, GenreDetEditDel


urlpatterns = [
    path("genre/", GenreAddList.as_view(), name="genre-added_list"),
    path("genre/<int:pk>", GenreDetEditDel.as_view(), name="genre-edit_del_edit"),
]
