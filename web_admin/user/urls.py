# web_admin/user/urls.py
from django.urls import path
from .views import UserView, toggle_user_status

app_name = 'user'

urlpatterns = [
    path('', UserView().list, name='user_list'),
    path('create/', UserView().form, name='user_create'),
    path('<int:id>/edit/', UserView().form, name='user_edit'),
    path('<int:id>/delete/', UserView().delete, name='user_delete'),
    path('<int:id>/toggle-status/', toggle_user_status, name='user_toggle_status'),
    path("datatable", UserView().datatable, name="user_datatable"),
]
