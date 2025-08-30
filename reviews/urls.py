from django.urls import path
from .views import ReviewAddList, ReviewDetEditDel

urlpatterns = [
    path("review/", ReviewAddList.as_view(), name="review-added_list" ),
    path("review/<int:pk>", ReviewDetEditDel.as_view(), name="review-edit_del_edit" ),
]