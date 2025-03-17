# web_admin/category/urls.py
from django.urls import path
from .views import PostView

app_name = 'post'

urlpatterns = [
    path('', PostView().list, name='post_list'),
    path('create/', PostView().form, name='post_create'),
    path('<int:id>/edit/', PostView().form, name='post_edit'),
    path('<int:id>/delete/', PostView().delete, name='post_delete'),
    path("datatable", PostView().datatable, name="post_datatable"),
]
