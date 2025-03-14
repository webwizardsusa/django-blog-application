from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='web_admin_dashboard'),
    path("auth/", include("web_admin.authentication.urls", namespace="authentication")),
    path('category/', include('web_admin.category.urls', namespace='category')),
    path('post/', include('web_admin.post.urls', namespace='post')),
    path('group/', include('web_admin.group.urls', namespace='group')),
    path('tag/', include('web_admin.tag.urls', namespace='tag')),
    path('user/', include('web_admin.user.urls', namespace='user')),
    path('myaccount/', include('web_admin.myaccount.urls', namespace='myaccount')),
]
