from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.db.models.query_utils import Q
from django.core.mail import BadHeaderError
from django.http import HttpResponse
from blog_application import settings
from .forms import AdminPasswordResetForm

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

    return render(request, "authentication/login.html")


def web_admin_logout(request):
    logout(request)
    return redirect("authentication:login")


def admin_password_reset_request(request):
    print("Password reset request received")  # Debug print
    if request.method == "POST":
        form = AdminPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            users = User.objects.filter(Q(email=email))
            if users.exists():
                for user in users:
                    subject = "Admin Password Reset Requested"
                    email_template_name = "authentication/reset_email.html"
                    context = {
                        "email": user.email,
                        'domain': request.get_host(),
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'https' if request.is_secure() else 'http',
                    }
                    email_content = render_to_string(email_template_name, context)
                    try:
                        email = EmailMessage(
                            subject,
                            email_content,
                            settings.DEFAULT_FROM_EMAIL,
                            [user.email]
                        )
                        email.content_subtype = "html"
                        email.send()
                        messages.success(request, "Password reset link has been sent to your email address.")
                        return redirect('authentication:login')
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
            else:
                messages.error(request, "No admin user found with that email address.")
    else:
        print("Creating new password reset form")  # Debug print
        form = AdminPasswordResetForm()
    
    print("Rendering forgot_password.html")  # Debug print
    return render(request, "authentication/forgot_password.html", {"form": form})

def admin_password_reset_confirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            
            if password1 and password2 and password1 == password2:
                user.set_password(password1)
                user.save()
                messages.success(request, 'Your password has been reset successfully!')
                return redirect('authentication:login')
            else:
                messages.error(request, 'Passwords do not match.')
        return render(request, 'authentication/new_password.html')
    else:
        messages.error(request, 'The reset link is invalid or has expired.')
        return redirect('authentication:login')
