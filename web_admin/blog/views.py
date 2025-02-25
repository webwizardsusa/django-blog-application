from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib import messages
from .models import Blog, Tag
from web_admin.category.models import Category
from .forms import BlogForm
from django.contrib.auth.models import User
from django.db.models import Q

def blog_list(request):
    categories = Category.objects.all()
    users = User.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/list.html', {"categories": categories, "users":users, "tags":tags})

def blog_list_json(request):
    blogs = Blog.objects.select_related("category", "author").all()
    order_column_index = int(request.GET.get('order[0][column]', 0))
    order_dir = request.GET.get('order[0][dir]', 'desc')
    search_value = request.GET.get("search[value]", "").strip() 

    
    column_mapping = {
        0: "title",
        1: "category__name",
        2: "image",
        3: "author__username",
        4: "is_published",
        5: "created_at",
    }
        
    order_column = column_mapping.get(order_column_index, "title")
    if order_dir == "desc":
        order_column = f"-{order_column}"
            
    blogs = blogs.order_by(order_column)
            
            
    category_id = request.GET.get("category")
    if category_id:
        blogs = blogs.filter(category_id=category_id)
        
    author_id = request.GET.get("author")
    if author_id:
        blogs = blogs.filter(author_id=author_id)
        
    tag_id = request.GET.get("tag")
    if tag_id:
        blogs = blogs.filter(tags__id=tag_id)

    if search_value:
        blogs = blogs.filter(Q(title__icontains=search_value) | Q(category__name__icontains=search_value) | Q(is_published__icontains=search_value) | Q(author__username__icontains=search_value) )
        
    paginator = Paginator(blogs, request.GET.get("length", 10))
    page_number = (int(request.GET.get("start", 0)) // paginator.per_page) + 1
    page_obj = paginator.get_page(page_number)

    
        
    data = [
        {
            "title": blog.title,
            "category": blog.category.name,
            "image": blog.image.url if blog.image else None,
            "author": blog.author.username,
            "status": "Published" if blog.is_published else "Draft",
            "created_at": blog.created_at.strftime("%Y-%m-%d %H:%M"),
            "edit_url": reverse("blog:blog_edit", kwargs={"pk": blog.pk}),
            "delete_url": reverse("blog:blog_delete", kwargs={"pk": blog.pk}),
        }
        for blog in page_obj.object_list
    ]

    return JsonResponse({"draw": int(request.GET.get("draw", 1)), "recordsTotal": blogs.count(), "recordsFiltered": paginator.count, "data": data,})

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