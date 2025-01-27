from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='web_admin_dashboard'),
    path("auth/", include("web_admin.authentication.urls", namespace="authentication")),
    path('category/', include('web_admin.category.urls', namespace='category')),
    path('blog/', include('web_admin.blog.urls', namespace='blog')),
    path('tag/', include('web_admin.tag.urls', namespace='tag')),
]
