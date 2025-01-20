from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path("blogs/", views.blog_list, name='blog_list'),
    # path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
