from django.shortcuts import render, get_object_or_404
from web_admin.blog.models import Blog, Category, Tag, User

def home(request):
    blogs = Blog.objects.filter(is_published=True).order_by("-created_at")
    featured_blog = blogs.first()
    recent_blogs = blogs[1:6]
    categories = Category.objects.all()
    tags = Tag.objects.all()

    trending_tag = Tag.objects.filter(name="trending").first()
    if trending_tag:
        trending_blogs = Blog.objects.filter(tags=trending_tag, is_published=True).order_by("-created_at")[:4]
    else:
        trending_blogs = []

    latest_blog_categories = Category.objects.all()[:6]  # Fetch only the first 6 categories
    latest_blogs_by_category = []

    for category in latest_blog_categories:
        latest_blog = Blog.objects.filter(category=category, is_published=True).order_by('-created_at').first()
        if latest_blog:
            latest_blogs_by_category.append(latest_blog)

    return render(request, "public_site/home.html", {
        "featured_blog": featured_blog, 
        "recent_blogs": recent_blogs, 
        "categories": categories,
        "latest_blogs_by_category": latest_blogs_by_category,
        "tags": tags,
        "trending_blogs": trending_blogs,
    })

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    categories = Category.objects.all()
    return render(request, 'public_site/blog_detail.html', {'blog': blog, 'categories': categories})

def blog_category(request, slug):
    category = get_object_or_404(Category.objects.prefetch_related('blogs'), slug=slug)
    recent_blogs = category.blogs.filter(is_published=True).order_by("-created_at")[:4]
    blogs = category.blogs.filter(is_published=True).order_by("-created_at")
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'public_site/blog_category.html', {
        'category': category,
        'blogs': blogs,
        'recent_blogs': recent_blogs,
        'categories': categories,
        'tags': tags,
    })

def blog_author(request, user_id):
    author = get_object_or_404(User, pk=user_id)
    recent_blogs = Blog.objects.filter(author=author, is_published=True).order_by("-created_at")[:4]
    blogs = Blog.objects.filter(author=author, is_published=True).order_by("-created_at")
    categories = Category.objects.all()
    tags = Tag.objects.all()
    print(author)
    return render(request, 'public_site/blog_author.html', {
        'author': author,
        'blogs': blogs,
        'categories': categories,
        'tags': tags,
        'recent_blogs': recent_blogs,
    })

def about_us(request):
    return render(request, 'public_site/about_us.html')

def contact_us(request):
    return render(request, 'public_site/contact_us.html')