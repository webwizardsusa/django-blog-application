from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Blog
from web_admin.category.models import Category
from .forms import BlogForm

def blog_list(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()

    category_id = request.GET.get("category")
    if category_id:
        blogs = blogs.filter(category_id=category_id)

    context = {
        "blogs": blogs,
        "categories": categories,
        "breadcrumb_title": "Blogs",
        "breadcrumbs": [
            {"name": "Blogs"}
        ]
    }

    return render(request, 'blog/list.html', context)

def blog_create(request):
    form = BlogForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Blog created successfully.")
            return redirect('blog:blog_list')

    context = {
        "form": form,
        "breadcrumb_title": "Blog Management",
        "breadcrumbs": [
            {"name": "Blogs", "url": reverse('blog:blog_list')},
            {"name": "Create Blog"}
        ]
    }
    return render(request, 'blog/form.html', context)

def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = BlogForm(request.POST or None, request.FILES or None, instance=blog)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Blog updated successfully.")
        return redirect("blog:blog_list")

    context = {
        "form": form,
        "blog": blog,
        "breadcrumb_title": "Blog Management",
        "breadcrumbs": [
            {"name": "Blogs", "url": reverse('blog:blog_list')},
            {"name": "Edit Blog"}
        ]
    }
    
    return render(request, "blog/form.html", context)

def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    messages.success(request, "Blog deleted successfully.")
    return redirect('blog:blog_list')