from django.urls import path
from .views import MovieAddList, MovieDetEditDel

urlpatterns = [
    path("movie/", MovieAddList.as_view(), name="movie-added_list" ),
    path("movie/<int:pk>", MovieDetEditDel.as_view(), name="movie-edit_del_edit" ),
]