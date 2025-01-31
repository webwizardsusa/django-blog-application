from django.shortcuts import render, get_object_or_404
from web_admin.blog.models import Blog, Category, Tag, User
from django.core.paginator import Paginator

def paginate_queryset(request, queryset, per_page):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)

def get_common_context():
    return {
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),
    }

def home(request):
    blogs = Blog.objects.filter(is_published=True).select_related("author", "category").prefetch_related("tags").order_by("-created_at")
    featured_blog = blogs.first()
    recent_blogs = blogs[1:6]

    trending_tag = Tag.objects.filter(name="trending").first()
    trending_blogs = blogs.filter(tags=trending_tag)[:4] if trending_tag else []

    latest_blog_categories = Category.objects.prefetch_related("blogs").all()[:6]
    latest_blogs_by_category = [
        category.blogs.filter(is_published=True).order_by('-created_at').first()
        for category in latest_blog_categories
    ]

    context = {
        "featured_blog": featured_blog,
        "recent_blogs": recent_blogs,
        "latest_blogs_by_category": [blog for blog in latest_blogs_by_category if blog],
        "trending_blogs": trending_blogs,
        **get_common_context(),
    }
    return render(request, "public_site/home.html", context)

def blog_detail(request, slug):
    blog = get_object_or_404(Blog.objects.select_related("author", "category").prefetch_related("tags"), slug=slug)
    context = {
        "blog": blog,
        **get_common_context(),
    }
    return render(request, "public_site/blog_detail.html", context)

def blog_category(request, slug):
    category = get_object_or_404(Category.objects.prefetch_related('blogs'), slug=slug)
    blogs = category.blogs.filter(is_published=True).select_related("author", "category").prefetch_related("tags").order_by("-created_at")
    page_obj = paginate_queryset(request, blogs, 10)
    recent_blogs = blogs[:4]

    context = {
        "category": category,
        "blogs": blogs,
        "page_obj": page_obj,
        "recent_blogs": recent_blogs,
        **get_common_context(),
    }
    return render(request, 'public_site/blog_category.html', context)

def blog_author(request, user_id):
    author = get_object_or_404(User, pk=user_id)
    blogs = Blog.objects.filter(author=author, is_published=True).select_related("category").prefetch_related("tags").order_by("-created_at")
    page_obj = paginate_queryset(request, blogs, 10)
    recent_blogs = blogs[:4]

    context = {
        "author": author,
        "blogs": blogs,
        "page_obj": page_obj,
        "recent_blogs": recent_blogs,
        **get_common_context(),
    }
    return render(request, 'public_site/blog_author.html', context)

def blog_tag(request, slug):
    tag = get_object_or_404(Tag.objects.prefetch_related('blogs'), slug=slug)  # 'blog_set' is the default reverse relation for the Blog model
    blogs = Blog.objects.filter(tags=tag, is_published=True).select_related("author", "category").prefetch_related("tags").order_by("-created_at")
    page_obj = paginate_queryset(request, blogs, 10)
    recent_blogs = blogs[:4]

    context = {
        "tag": tag,
        "blogs": blogs,
        "page_obj": page_obj,
        "recent_blogs": recent_blogs,
        **get_common_context(),
    }
    return render(request, 'public_site/blog_tag.html', context)
