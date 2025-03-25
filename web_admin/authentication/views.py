from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.db import IntegrityError
from web_admin.user.models import Profile
from .tasks import send_registration_email

# Create your views here.
def web_admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()

        if user and not user.is_active:
            messages.error(request, "Your account is inactive. Please contact the administrator.")
        elif not user or authenticate(request, username=username, password=password) is None:
            messages.error(request, "Invalid username or password.")
        else:
            login(request, user)
            return redirect("web_admin_dashboard")

        return redirect("authentication:login")

    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username, email = request.POST.get("username").strip(), request.POST.get("email").strip()
        password1, password2 = request.POST.get("password1"), request.POST.get("password2")

        if len(password1) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
        elif password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
        else:
            try:
                user = User.objects.create_user(username=username, email=email, password=password1, is_active=False)
                user.groups.add(Group.objects.get_or_create(name="Author")[0])
                Profile.objects.create(user=user, image="profile_pics/default.jpg", description="")

                send_registration_email.delay(username, email, request.build_absolute_uri(reverse("authentication:login")))

                messages.success(request, "Registration successful! Please wait for account activation.")
                return redirect("authentication:login")
            except IntegrityError:
                messages.error(request, "An error occurred during registration.")

        return redirect("authentication:register")

    return render(request, "register.html")

def web_admin_logout(request):
    logout(request)
    return redirect("authentication:login")
