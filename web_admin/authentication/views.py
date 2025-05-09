from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.db import IntegrityError
from web_admin.user.models import Profile
from .tasks import send_registration_email
from .forms import LoginForm, RegistrationForm

# Create your views here.
def web_admin_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = User.objects.filter(username=username).first()

            if user and not user.is_active:
                messages.error(request, "Your account is inactive. Please contact the administrator.")
            elif not user or authenticate(request, username=username, password=password) is None:
                messages.error(request, "Invalid username or password.")
            else:
                login(request, user)
                return redirect("web_admin_dashboard")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            try:
                user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password1'], first_name=data['firstname'], last_name=data['lastname'], is_active=False)
                user.groups.add(Group.objects.get_or_create(name="Author")[0])
                Profile.objects.create(user=user, image="profile_pics/default.jpg", description="")

                send_registration_email.delay(data['username'], data['email'], request.build_absolute_uri(reverse("authentication:login")))

                messages.success(request, "Registration successful! Please wait for account activation.")
                return redirect("authentication:login")
            except IntegrityError:
                messages.error(request, "An error occurred during registration.")
        else:
            for field_errors in form.errors.values():
                for error in field_errors:
                    messages.error(request, error)

    else:
        form = RegistrationForm()

    return render(request, "register.html", {"form": form})

def web_admin_logout(request):
    logout(request)
    return redirect("authentication:login")
