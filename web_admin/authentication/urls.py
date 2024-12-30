from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path("login/", views.web_admin_login, name="login"),
    path("logout/", views.web_admin_logout, name="logout"),
]
