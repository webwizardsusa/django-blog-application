from django.contrib.auth.models import User, Group
from web_admin.common.crud_views import CrudView
from web_admin.category.models import Category
from web_admin.tag.models import Tag 
from .models import Post
from .forms import PostForm

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
    
    def _page_filter(self, query, user):
        """Filter the query based on the user's role."""
        if user.groups.filter(name="author").exists():
            return query.filter(author=user)  
        elif user.groups.filter(name="web_admin").exists():
            return query

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
