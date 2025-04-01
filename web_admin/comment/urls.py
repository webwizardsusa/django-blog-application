from django.urls import path
from .views import CommentView
app_name = 'comment'

urlpatterns = [
    path('', CommentView().list, name='comment_list'),
    path('<int:id>/delete/', CommentView().delete, name='comment_delete'),
    path("datatable", CommentView().datatable, name="comment_datatable"),
]
