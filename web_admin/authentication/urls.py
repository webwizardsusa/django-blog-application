from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path("login/", views.web_admin_login, name="login"),
    path("logout/", views.web_admin_logout, name="logout"),
    path('password-reset/', views.admin_password_reset_request, name='reset_password'),
    path('password-reset-confirm/<uidb64>/<token>/', views.admin_password_reset_confirm, name='password_reset_confirm'),
]
