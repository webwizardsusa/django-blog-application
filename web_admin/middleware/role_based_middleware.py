from django.shortcuts import redirect
from django.http import HttpResponseForbidden

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        # Exclude login pages from checks to prevent infinite redirects
        if path.startswith("/web_admin/auth/login/") or path.startswith("/admin/login/"):
            return self.get_response(request)

        # Handle /web_admin role restrictions
        if path.startswith("/web_admin"):
            if not request.user.is_authenticated:
                return redirect("/web_admin/auth/login/")

        # Handle /admin role restrictions
        elif path.startswith("/admin"):
            if not request.user.is_authenticated:
                return redirect("/admin/login/")
            if not (request.user.is_superuser or request.user.groups.filter(name="admin").exists()):
                return HttpResponseForbidden("You do not have permission to access this page.")

        return self.get_response(request)
