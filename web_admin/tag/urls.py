# web_admin/tag/urls.py
from django.urls import path
from .views import TagView

app_name = 'tag'

urlpatterns = [
    path('', TagView().list, name='tag_list'),
    path('create/', TagView().form, name='tag_create'),
    path('<int:id>/edit/', TagView().form, name='tag_edit'),
    path('<int:id>/delete/',  TagView().delete, name='tag_delete'),
    path("datatable", TagView().datatable, name="tag_datatable"),
]