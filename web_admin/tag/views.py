from web_admin.common.crud_views import CrudView
from django.db.models import Count
from .models import Tag
from .forms import TagForm

class TagView(CrudView):
    module = 'Tag'
    model = Tag
    form_class = TagForm
    list_template_name = 'tag/list.html' 
    form_template_name = 'tag/form.html'
    redirect_url = 'tag:tag_list'

    def _shareData(self, page, data = {}):
        if page == 'List':
            return {
                'columns': ["Name", "Total Posts", "Actions"],
            }
        
    def _dt(self):
        return {
            'sort': ['name'],
            'search': ['name__icontains'],
            'select': ['id', 'name', 'total_posts'], 
            'query': self.model.objects.annotate( total_posts=Count('posts') ).values('id', 'name', 'total_posts')     
        }
