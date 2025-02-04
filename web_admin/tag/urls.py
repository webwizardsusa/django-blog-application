# web_admin/tag/urls.py
from django.urls import path
from .views import TagCrud

app_name = 'tag'

urlpatterns = [
    path('', TagCrud().list, name='tag_list'), 
    path('create/', TagCrud().create, name='tag_create'),
    path('<int:pk>/edit/', TagCrud().edit, name='tag_edit'),
    path('<int:pk>/delete/', TagCrud().delete, name='tag_delete'),
]