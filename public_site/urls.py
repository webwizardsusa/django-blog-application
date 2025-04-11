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
    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),
    # path("posts/", views.post_list, name='post_list'),
    # path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='user_logout'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/like/', views.like_post, name="like_post"),
    path('password-reset/', views.password_reset_request, name='password_reset'),
    path('password-reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
]
