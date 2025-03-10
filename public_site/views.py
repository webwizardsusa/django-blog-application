import random
from django.shortcuts import render, redirect, get_object_or_404
from web_admin.post.models import Post, Category, Tag, User
from django.contrib.auth.models import Group 
from django.core.paginator import Paginator
from public_site.contact.forms import ContactForm
from django.contrib import messages
from public_site.tasks import send_contact_email_task
from django.core.mail import send_mail
from blog_application import settings
from django.core.mail import EmailMessage

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
    posts = Post.objects.filter(is_published=True).select_related("author", "category").prefetch_related("tags").order_by("-created_at")
    featured_post = random.choice(posts) if posts else None
    recent_posts = posts[1:6]

    trending_tag = Tag.objects.filter(name="trending").first()
    trending_posts = posts.filter(tags=trending_tag)[:4] if trending_tag else []

    latest_post_categories = Category.objects.prefetch_related("posts").all()[:6]
    latest_posts_by_category = [
        category.posts.filter(is_published=True).order_by('-created_at').first()
        for category in latest_post_categories
    ]

    context = {
        "featured_post": featured_post,
        "recent_posts": recent_posts,
        "latest_posts_by_category": [post for post in latest_posts_by_category if post],
        "trending_posts": trending_posts,
        **get_common_context(),
    }
    return render(request, "public_site/home.html", context)

def post_detail(request, slug):
    post = get_object_or_404(Post.objects.select_related("author", "category").prefetch_related("tags"), slug=slug)
    context = {
        "post": post,
        **get_common_context(),
    }
    return render(request, "public_site/post_detail.html", context)

def post_category(request, slug):
    category = get_object_or_404(Category.objects.prefetch_related('posts'), slug=slug)
    posts = category.posts.filter(is_published=True).select_related("author", "category").prefetch_related("tags").order_by("-created_at")
    page_obj = paginate_queryset(request, posts, 10)
    recent_posts = posts[:4]

    context = {
        "category": category,
        "posts": page_obj.object_list,
        "page_obj": page_obj,
        "recent_posts": recent_posts,
        **get_common_context(),
    }
    return render(request, 'public_site/post_category.html', context)

def post_author(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author, is_published=True).select_related("category").prefetch_related("tags").order_by("-created_at")
    page_obj = paginate_queryset(request, posts, 10)
    recent_posts = posts[:4]

    context = {
        "author": author,
        "posts": page_obj.object_list,
        "page_obj": page_obj,
        "recent_posts": recent_posts,
        **get_common_context(),
    }
    return render(request, 'public_site/post_author.html', context)

def post_tag(request, slug):
    tag = get_object_or_404(Tag.objects.prefetch_related('posts'), slug=slug)  # 'post_set' is the default reverse relation for the Post model
    posts = Post.objects.filter(tags=tag, is_published=True).select_related("author", "category").prefetch_related("tags").order_by("-created_at")
    page_obj = paginate_queryset(request, posts, 10)
    recent_posts = posts[:4]

    context = {
        "tag": tag,
        "posts": page_obj.object_list,
        "page_obj": page_obj,
        "recent_posts": recent_posts,
        **get_common_context(),
    }
    return render(request, 'public_site/post_tag.html', context)

def post_search(request):
    search_query = request.GET.get('search', '')  
    if search_query:
        posts = Post.objects.filter(title__icontains=search_query)  
    page_obj = paginate_queryset(request, posts, 10)


    context = {
        "posts": page_obj.object_list,
        "page_obj": page_obj,
        "search": search_query,
        **get_common_context(),
    }
    return render(request, 'public_site/post_search.html', context)
    
def about_us(request):
    authors = User.objects.all().filter(groups=2)[:6]

    context = {   
        **get_common_context(),
        "authors": authors,
    }
    return render(request, 'public_site/about_us.html', context)

def contact_us(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            
            context = { 
                **get_common_context(),
            }
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            from_email = request.POST.get('email')
            recipient_list = [settings.DEFAULT_FROM_EMAIL]
            # Call the Celery task to send the email asynchronously
            # send_contact_email_task.delay(subject, message, from_email, recipient_list)
            send_mail(subject, message, from_email, recipient_list)
            # email = EmailMessage(subject, message, from_email, recipient_list)
            # email.content_subtype = 'html'  # Important for HTML emails
            # email.send()
    
            messages.success(request, "Thanks for Contact Us.")
            return redirect('/contact-us/#contact_form')
        
    context = {
        "form":form,   
        **get_common_context(),
    }
    return render(request, 'public_site/contact_us.html', context)
