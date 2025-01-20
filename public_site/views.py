from django.shortcuts import render, get_object_or_404
from web_admin.blog.models import Blog

def home(request):
    blogs = Blog.objects.filter(is_published=True).order_by("-created_at")[:5]
    return render(request, "public_site/home.html", {"blogs": blogs})