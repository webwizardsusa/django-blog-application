from web_admin.common.crud_views import CrudView
from django.contrib.auth.models import User
from .forms import UserForm

class UserView(CrudView):
    module = 'User'
    model = User
    form_class = UserForm
    list_template_name = 'user/list.html' 
    form_template_name = 'user/form.html'
    redirect_url = 'user:user_list'

    def _shareData(self, page, data = {}):
        if page == 'List':
            return {
                'columns': ["Username", "Email", "First Name", "Last Name", "Status", "Actions"],
            }
        
    def _dt(self):
        return {
            'sort': ['username', 'email', 'first_name', 'last_name', 'is_active'],  
            'search': ['username__icontains', 'email__icontains', 'first_name__icontains', 'last_name__icontains'],
            'select': ['id', 'username', 'email', 'first_name', 'last_name', 'is_active'], 
            'query' : self.model.objects.filter(is_superuser=False)
        }