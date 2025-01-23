from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('category/<str:name>/', views.blog_category, name='blog_category'),
    # path("blogs/", views.blog_list, name='blog_list'),
    # path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
