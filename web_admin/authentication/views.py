from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def web_admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("web_admin_dashboard")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")


def web_admin_logout(request):
    logout(request)
    return redirect("authentication:login")
