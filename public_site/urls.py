from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('listing/', views.post_search, name='post_search'),
    path('category/<slug:slug>/', views.post_category, name='post_category'),
    path('author/<str:username>/', views.post_author, name='post_author'),
    path('tag/<slug:slug>/', views.post_tag, name='post_tag'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    # path("posts/", views.post_list, name='post_list'),
    # path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
]
