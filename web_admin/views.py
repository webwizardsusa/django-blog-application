from django.contrib.auth.models import User, Group
from django.shortcuts import render
from web_admin.blog.models import Blog 
from web_admin.category.models import Category 
from web_admin.tag.models import Tag 

def dashboard(request):
    blogs = Blog.objects.order_by('-created_at')[:6] 
    total_blogs = Blog.objects.count()  
    users_count = User.objects.filter(groups__id=2, is_active=1).count()
    total_category = Category.objects.count() 
    total_tags = Tag.objects.count()

    return render(request, 'dashboard.html', {'blogs': blogs, 'total_blogs': total_blogs, 'users_count': users_count, 'total_category': total_category, 'total_tags': total_tags })