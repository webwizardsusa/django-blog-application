from django.shortcuts import render, get_object_or_404
from web_admin.blog.models import Blog
from web_admin.blog.models import Category

def home(request):
    # blogs = Blog.objects.filter(is_published=True).order_by("-created_at")[:5]
    featured_blog = Blog.objects.filter(is_published=True).order_by("-created_at").first()
    recent_blogs = Blog.objects.filter(is_published=True).order_by("-created_at")[1:6]
    return render(request, "public_site/home.html", {"featured_blog": featured_blog, "recent_blogs": recent_blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'public_site/blog_detail.html', {'blog': blog})

def blog_category(request, name):
    category = get_object_or_404(Category, name=name)
    blogs = category.blogs.filter(is_published=True).order_by("-created_at")
    return render(request, 'public_site/blog_category.html', {'category': category, 'blogs': blogs})