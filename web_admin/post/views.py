from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib import messages
from .models import Post
from web_admin.category.models import Category
from .forms import PostForm

def post_list(request):
    categories = Category.objects.all()
    return render(request, 'post/list.html', {"categories": categories})

def post_list_json(request):
    posts = Post.objects.select_related("category", "author").all()
    order_column_index = int(request.GET.get('order[0][column]', 0))
    order_dir = request.GET.get('order[0][dir]', 'desc')
    
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
            
    posts = posts.order_by(order_column)
            
            
    category_id = request.GET.get("category")
    if category_id:
        posts = posts.filter(category_id=category_id)

    paginator = Paginator(posts, request.GET.get("length", 10))
    page_number = (int(request.GET.get("start", 0)) // paginator.per_page) + 1
    page_obj = paginator.get_page(page_number)

    data = [
        {
            "title": post.title,
            "category": post.category.name,
            "image": post.image.url if post.image else None,
            "author": post.author.username,
            "status": "Published" if post.is_published else "Draft",
            "created_at": post.created_at.strftime("%d-%m-%Y"),
            "edit_url": reverse("post:post_edit", kwargs={"pk": post.pk}),
            "delete_url": reverse("post:post_delete", kwargs={"pk": post.pk}),
        }
        for post in page_obj.object_list
    ]

    return JsonResponse({"draw": int(request.GET.get("draw", 1)), "recordsTotal": posts.count(), "recordsFiltered": paginator.count, "data": data,})

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Post created successfully.")
            return redirect('post:post_list')

    context = {
        "form": form,
        "breadcrumb_title": "Post Management",
        "breadcrumbs": [
            {"name": "Posts", "url": reverse('post:post_list')},
            {"name": "Create Post"}
        ]
    }
    return render(request, 'post/form.html', context)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Post updated successfully.")
        return redirect("post:post_list")

    context = {
        "form": form,
        "post": post,
        "breadcrumb_title": "Post Management",
        "breadcrumbs": [
            {"name": "posts", "url": reverse('post:post_list')},
            {"name": "Edit Post"}
        ]
    }
    
    return render(request, "post/form.html", context)

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, "Post deleted successfully.")
    return redirect('post:post_list')