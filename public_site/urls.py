from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('listing/', views.blog_search, name='blog_search'),
    path('category/<slug:slug>/', views.blog_category, name='blog_category'),
    path('author/<int:user_id>/', views.blog_author, name='blog_author'),
    path('tag/<slug:slug>/', views.blog_tag, name='blog_tag'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    # path("blogs/", views.blog_list, name='blog_list'),
    # path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
