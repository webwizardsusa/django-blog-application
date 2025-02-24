from django.urls import path
from . import views

app_name = 'myaccount'

urlpatterns = [
    path('', views.edit_profile, name='edit_profile'),
]