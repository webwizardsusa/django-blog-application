from django.shortcuts import render
from .decorators import web_admin_login_required

@web_admin_login_required
def dashboard(request):
    return render(request, 'dashboard.html')