import random
from django.shortcuts import render, redirect, get_object_or_404, reverse
from web_admin.post.models import Post, Category, Tag
from web_admin.user.models import Profile
from django.contrib.auth.models import Group , User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.db import IntegrityError
from public_site.contact.forms import ContactForm
from django.contrib import messages
from django.utils.timezone import now
from public_site.tasks import send_contact_email_task, send_register_email
from django.core.mail import send_mail
from blog_application import settings
from django.core.mail import EmailMessage
from .models import Comment , Like 
from web_admin.post.models import Post
from django.http import JsonResponse

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
    posts = Post.objects.filter(is_published=True, published_at__lte=now()).select_related("author", "category").prefetch_related("tags").order_by("-published_at")
    featured_post = random.choice(posts) if posts else None
    recent_posts = posts[1:6]

    trending_tag = Tag.objects.filter(name="trending").first()
    trending_posts = posts.filter(tags=trending_tag)[:4] if trending_tag else []

    latest_post_categories = Category.objects.prefetch_related("posts").all()[:6]
    latest_posts_by_category = [
        category.posts.filter(is_published=True, published_at__lte=now()).order_by('-created_at').first()
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
    post = get_object_or_404(Post.objects.select_related("author", "category").prefetch_related("tags"), slug=slug, is_published=True, published_at__lte=now()) 
    comments = post.comments.all() 
    has_liked = False
    if request.user.is_authenticated:
        has_liked = post.likes.filter(user=request.user).exists()
    total_likes = post.likes.count()

    context = {
        "post": post,
        "comments": comments,
        "has_liked": has_liked, 
        "total_likes": total_likes,
        **get_common_context(),
    }
    return render(request, "public_site/post_detail.html", context)

def post_category(request, slug):
    category = get_object_or_404(Category.objects.prefetch_related('posts'), slug=slug)
    posts = category.posts.filter(is_published=True, published_at__lte=now()).select_related("author", "category").prefetch_related("tags").order_by("-created_at")
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
    posts = Post.objects.filter(author=author, is_published=True, published_at__lte=now()).select_related("category").prefetch_related("tags").order_by("-created_at")
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
    posts = Post.objects.filter(tags=tag, is_published=True, published_at__lte=now()).select_related("author", "category").prefetch_related("tags").order_by("-created_at")
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

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()

        if user and not user.is_active:
            messages.error(request, "Your account is inactive. Please contact the administrator.")
        elif not user or authenticate(request, username=username, password=password) is None:
            messages.error(request, "Invalid username or password.")
        else:
            login(request, user)
            return redirect("home")

        return redirect("user_login")
    return render(request, 'public_site/login.html')

def register(request):
    if request.method == "POST":
        username, email = request.POST.get("username").strip(), request.POST.get("email").strip()
        password1, password2 = request.POST.get("password1"), request.POST.get("password2")

        if len(password1) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
        elif password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
        else:
            try:
                user = User.objects.create_user(username=username, email=email, password=password1, is_active=False)
                user.groups.add(Group.objects.get_or_create(name="user")[0])
                Profile.objects.create(user=user, image="profile_pics/default.jpg", description="")
                send_register_email.delay(username, email, request.build_absolute_uri(reverse("user_login")))

                messages.success(request, "Registration successful! Please Login.")
                return redirect("user_login")
            except IntegrityError:
                messages.error(request, "An error occurred during registration.")

        return redirect("register")
    return render(request, 'public_site/register.html')

def user_logout(request):
    logout(request)
    return redirect("user_login")

def add_comment(request, post_id):
    if not request.user.is_authenticated:
        return JsonResponse({"success": False, "message": "You must be logged in to comment!"}, status=403)

    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        comment_text = request.POST.get("comment", "").strip()

        if comment_text:
            comment = Comment.objects.create(post=post, user=request.user, text=comment_text)
            return JsonResponse({"success": True, "message": "Comment added successfully!",
                "comment": {"user": comment.user.username, "text": comment.text, "created_at": comment.created_at.strftime("%Y-%m-%d %H:%M"),},
                "total_comments": post.comments.count()
            })
        else:
            return JsonResponse({"success": False, "message": "Comment cannot be empty!"}, status=400)

    return JsonResponse({"success": False, "message": "Invalid request!"}, status=400)

def like_post(request, post_id):
    if not request.user.is_authenticated:
     return JsonResponse({"redirect_url": "/login/"}, status=403)

    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    total_likes = post.likes.count() 

    return JsonResponse({"liked": liked, "total_likes": total_likes})
