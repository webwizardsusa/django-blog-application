from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='web_admin_dashboard'),
]
