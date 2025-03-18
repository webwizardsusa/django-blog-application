from web_admin.common.crud_views import CrudView
from django.db.models import Count
from .models import Category
from .forms import CategoryForm

class CategoryView(CrudView):
    module = 'Category'
    model = Category
    form_class = CategoryForm
    list_template_name = 'list.html' 
    form_template_name = 'form.html'
    redirect_url = 'category:category_list'

    def _shareData(self, page, data = {}):
        if page == 'List':
            return {
                'columns': ["Name","Total Posts", "Image", "Created At", "Actions"],
            }
    
    def _dt(self):
        return {
            'sort': ['name', 'total_posts', 'image', 'created_at'],
            'search': ['name__icontains'],
            'select': ['id', 'name', 'total_posts', 'image', 'created_at'], 
            'query': self.model.objects.annotate( total_posts=Count('posts') ).values('id', 'name', 'total_posts', 'image', 'created_at')     
        }

