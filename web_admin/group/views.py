from web_admin.common.crud_views import CrudView
from django.contrib.auth.models import Group
from .forms import GroupForm

class GroupView(CrudView):
    module = 'Group'
    model = Group
    form_class = GroupForm
    list_template_name = 'group/list.html' 
    form_template_name = 'group/form.html'
    redirect_url = 'group:group_list'

    def _shareData(self, page, data = {}):
        if page == 'List':
            return {
                'columns': ["Name", "Actions"],
            }
        
    def _dt(self):
        return {
            'sort': ['name'],
            'search': ['name__icontains'],
            'select': ['id', 'name'], 
            'query': self.model.objects.all()   
        }