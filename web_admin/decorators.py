from django.shortcuts import redirect
from django.http import HttpResponseForbidden

def web_admin_login_required(view_func):
    """
    Custom decorator to ensure the user is authenticated and belongs to the web_admin role.
    """
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return redirect("authentication:login")  # Redirect to the web admin login page
        
        # Check if the user belongs to the web_admin group
        if not request.user.groups.filter(name="web_admin").exists():
            return HttpResponseForbidden("You are not authorized to access this page.")  # Restrict access
        
        # If checks pass, proceed with the view
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view
