from web_admin.common.crud_views import CrudView
from public_site.models import Comment

class CommentView(CrudView):
    module = 'Comment'
    model = Comment
    list_template_name = 'comment/list.html' 
    redirect_url = 'comment:comment_list'

    def _shareData(self, page, data = {}):
        if page == 'List':
            return {
                'columns': ["Text", "Post", "Username", "Created At", "Actions"],
            }
        
    def _dt(self):
        return {
            'sort': ['text', 'created_at', 'post__title', 'user__username'], 
            'search': ['text__icontains', 'post__title__icontains', 'user__username__icontains'],  
            'select': ['id', 'text', 'created_at', 'post__title', 'user__username'], 
            'query': self.model.objects.select_related('post', 'user').all()  
        }