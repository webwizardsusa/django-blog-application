from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MyaccountForm, PasswordChangeForm

def edit_profile(request):
    user = request.user

    if request.method == "POST" and "update_profile" in request.POST:
        form = MyaccountForm(request.POST, instance=user)
        password_form = PasswordChangeForm(user) 
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('myaccount:edit_profile')  
    else:
        form = MyaccountForm(instance=user)

    if request.method == "POST" and "change_password" in request.POST:
        form = MyaccountForm(instance=user) 
        password_form = PasswordChangeForm(user, request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, "Password changed successfully.")
            return redirect('myaccount:edit_profile')
    else:
        password_form = PasswordChangeForm(user)

    context = {
        "form": form,
        "password_form": password_form,
        "breadcrumb_title": "My Account",
        "breadcrumbs": [
            {"name": "My Account", "url": reverse('myaccount:edit_profile')},
            {"name": "Edit Profile"}
        ]
    }
    return render(request, "myaccount/form.html", context)
