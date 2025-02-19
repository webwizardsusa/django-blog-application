from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='web_admin_dashboard'),
    path("auth/", include("web_admin.authentication.urls", namespace="authentication")),
    path('category/', include('web_admin.category.urls', namespace='category')),
    path('blog/', include('web_admin.blog.urls', namespace='blog')),
    path('tag/', include('web_admin.tag.urls', namespace='tag')),
    path('user/', include('web_admin.user.urls', namespace='user')),
    path('myaccount/', include('web_admin.myaccount.urls', namespace='myaccount')),
    path('news_letter/', include('web_admin.news_letter.urls', namespace='news_letter')),
]
