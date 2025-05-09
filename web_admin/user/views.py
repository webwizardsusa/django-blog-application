from web_admin.common.crud_views import CrudView
from django.contrib.auth.models import User
from .forms import UserForm
from django.db import models
from django.http import JsonResponse
from django.views.decorators.http import require_POST

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
                'columns': ["Username", "Email", "First Name", "Last Name", "Role", "Status", "Actions"],
            }
        
    def _dt(self):
        return {
            'sort': ['username', 'email', 'first_name', 'last_name', 'is_active', 'role'],  
            'search': ['username__icontains', 'email__icontains', 'first_name__icontains', 'last_name__icontains', 'groups__name__icontains'],
            'select': ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'is_active'], 
            'query': self.model.objects.filter(is_superuser=False).annotate(
                role=models.F('groups__name')
            ).values('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'role').distinct()
        }

@require_POST
def toggle_user_status(request, id):
    try:
        user = User.objects.get(id=id)
        user.is_active = not user.is_active
        user.save()
        return JsonResponse({'success': True})
    except User.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)