from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<slug:slug>/', views.blog_category, name='blog_category'),
    path('author/<int:user_id>/', views.blog_author, name='blog_author'),
    # path("blogs/", views.blog_list, name='blog_list'),
    # path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
