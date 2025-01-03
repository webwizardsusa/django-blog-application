# web_admin/category/urls.py
from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('create/', views.category_create, name='category_create'),
    path('<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('<int:pk>/delete/', views.category_delete, name='category_delete'),
]
