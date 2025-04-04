# web_admin/category/urls.py
from django.urls import path
from .views import PostView
from . import views
app_name = 'post'

urlpatterns = [
    path('', PostView().list, name='post_list'),
    path('create/', PostView().form, name='post_create'),
    path('<int:id>/edit/', PostView().form, name='post_edit'),
    path('<int:id>/delete/', PostView().delete, name='post_delete'),
    path("datatable", PostView().datatable, name="post_datatable"),
    path('category/create/', views.create_category, name='create_category'),
    path('author/create/', views.create_author, name='create_author'),
    path('tag/create/', views.create_tag, name='create_tag'),
]
