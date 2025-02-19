# web_admin/category/urls.py
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'news_letter'

urlpatterns = [
    path('', views.news_letters_list, name='news_letters_list'),
    path('create/', views.news_letter_create, name='news_letter_create'),
    # path('<int:pk>/edit/', views.news_letter_edit, name='news_letter_edit'),
    # path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)