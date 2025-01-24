# web_admin/author/urls.py
from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('', views.author_list, name='author_list'),
    path('create/', views.author_create, name='author_create'),
    path('<int:pk>/edit/', views.author_edit, name='author_edit'),
    path('<int:pk>/delete/', views.author_delete, name='author_delete'),
]
