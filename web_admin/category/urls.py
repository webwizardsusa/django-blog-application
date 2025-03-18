# web_admin/category/urls.py
from django.urls import path
from .views import CategoryView

app_name = 'category'

urlpatterns = [
    path('', CategoryView().list, name='category_list'),
    path('create/', CategoryView().form, name='category_create'),
    path('<int:id>/edit/', CategoryView().form, name='category_edit'),
    path('<int:id>/delete/', CategoryView().delete, name='category_delete'),
    path("datatable", CategoryView().datatable, name="category_datatable"),
]
