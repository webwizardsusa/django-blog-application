# web_admin/tag/urls.py
from django.urls import path
from . import views

app_name = 'tag'

urlpatterns = [
    path('', views.tag_list, name='tag_list'),
    path('create/', views.tag_create, name='tag_create'),
    path('<int:pk>/edit/', views.tag_edit, name='tag_edit'),
    path('<int:pk>/delete/', views.tag_delete, name='tag_delete'),
]