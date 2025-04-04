from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.shortcuts import render, redirect
from web_admin.common.crud_views import CrudView
from web_admin.category.models import Category
from web_admin.user.models import Profile
from web_admin.tag.models import Tag 
from .models import Post
from .forms import PostForm, CategoryForm

def create_category(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        description = request.POST.get("description", "").strip()
        
        errors = {}

        if Category.objects.filter(name__iexact=name).exists():
            errors["name"] = "Category name already exists."

        if not name:
            errors["name"] = "Category name is required."

        if not description:
            errors["description"] = "Description is required."

        if errors:
            return JsonResponse({"success": False, "errors": errors}, status=400)

        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return JsonResponse({
                "success": True,
                "id": category.id,
                "name": category.name
            })
        
        return JsonResponse({"success": False, "errors": form.errors}, status=400)

    return JsonResponse({"success": False, "errors": {"error": "Invalid request"}}, status=400)


def create_author(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        description = request.POST.get("description", "").strip()

        errors = {}

        if not username:
            errors["username"] = "Username is required."
        elif User.objects.filter(username=username).exists():
            errors["username"] = "Username already exists."

        if not email:
            errors["email"] = "Email is required."
        elif User.objects.filter(email=email).exists():
            errors["email"] = "Email already exists."

        if not description:
            errors["description"] = "Description is required."

        if errors:
            return JsonResponse(errors, status=400) 

        user = User.objects.create_user(username=username, email=email, password="12345678")
        user.is_active = True
        user.save()

        author_group, _ = Group.objects.get_or_create(name="author")
        user.groups.add(author_group)

        Profile.objects.create(user=user, description=description)

        return JsonResponse({
            "success": True,
            "id": user.id,  
            "username": user.username  
        })

    return JsonResponse({"error": "Invalid request"}, status=400)

def create_tag(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        errors = {}

        if not name:
            errors["name"] = "Name is required."
            return JsonResponse({"errors": errors}, status=400)

        tag, created = Tag.objects.get_or_create(name=name)

        if created:
            return JsonResponse({"success": True, "id": tag.id, "name": tag.name})
        else:
            return JsonResponse({"errors": {"name": "Tag already exists."}}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)

class PostView(CrudView):
    module = 'Post'
    model = Post
    form_class = PostForm
    list_template_name = 'post/list.html' 
    form_template_name = 'post/form.html'
    redirect_url = 'post:post_list'

    def _shareData(self, page, data = {}):
        if page == 'List':
            return {
                'columns': ["Title", "Category", "Image", "Author", "Status", "Created At", "Actions"],
            }
        
    def _dt(self):
        return {
            'sort': ['title', 'image', 'category__name', 'author__username', 'is_published', 'created_at'],  
            'search': ['title__icontains', 'category__name__icontains', 'author__username__icontains'],  
            'select': ['id', 'title', 'image', 'category__name', 'author__username', 'is_published', 'created_at'], 
            'query': self.model.objects.select_related('category', 'author').all()  
        }

    def _query(self, page, id=None): 
        if page == 'List':
            authors_group = Group.objects.filter(name="author").first() 
            authors = User.objects.filter(groups=authors_group) if authors_group else User.objects.none()

            return {'categories': Category.objects.all(), 'authors': authors, 'tags': Tag.objects.all()}
            
        return None

    def _filter(self, query, request):
        category_name = request.POST.get('category') or None  
        author_username = request.POST.get('author') or None
        tag_name = request.POST.get('tag') or None

        if category_name:
            query = query.filter(category__name=category_name)  

        if author_username:
            query = query.filter(author__username=author_username)

        if tag_name:
            query = query.filter(tags__name=tag_name) 

        return query

    def post(self, request, id=None):
        if id:
            instance = self.model.objects.get(id=id)
            form = self.form_class(request.POST, request.FILES, instance=instance)
        else:
            form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(self.redirect_url)
        else:
            # If form is invalid, re-render the template with errors
            context = {
                'form': form,
                'title': f"{'Edit' if id else 'Add'} {self.module}",
                'id': id
            }
            if hasattr(self, '_query'):
                context.update(self._query('Form', id))
            return render(request, self.form_template_name, context)
