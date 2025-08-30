from django.urls import path
from .views import ActorsAddList, ActorsDetEditDel

urlpatterns = [
    path("actors/", ActorsAddList.as_view(), name="actors-added_list" ),
    path("actors/<int:pk>", ActorsDetEditDel.as_view(), name="actors-edit_del_edit" ),
]