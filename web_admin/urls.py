from django.urls import path, include
from . import views

urlpatterns = [
    path("auth/", include("web_admin.authentication.urls", namespace="authentication")),
    path('', views.dashboard, name='web_admin_dashboard'),
]
