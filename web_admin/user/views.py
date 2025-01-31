# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User, Group
from .forms import UserForm, UserUpdateForm, ProfileForm
from django.http import HttpResponse
from django.contrib import messages

def user_list(request):
    users = User.objects.all().filter(groups=2)
    context = {
        "users": users,
        "breadcrumb_title": "Users",
        "breadcrumbs": [
            {"name": "Users"}
        ]
    }

    return render(request, 'user/list.html', {'context':context})

def user_create(request):
    form = UserForm(request.POST or None, request.FILES or None)
    profile_form = ProfileForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST":
        print(request.POST, request.FILES)

        form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user 
            profile.save()

            group = Group.objects.get(id=2)
            group.user_set.add(user)  
            messages.success(request, "User created successfully.")
            return redirect('user:user_list')
    else:
        form = UserForm()
        profile_form = ProfileForm()

    context = {
        "form": form,
        "profile_form": profile_form,
        "breadcrumb_title": "User Management",
        "breadcrumbs": [
            {"name": "Users", "url": reverse('user:user_list')},
            {"name": "Create User"}
        ]
    }
    return render(request, 'user/form.html', context)

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile) 
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            messages.success(request, "User updated successfully.")
            return redirect('user:user_list')
    else:
        form = UserUpdateForm(instance=user)
        profile_form = ProfileForm(instance=user.profile) 

    context = {
        "form": form,
        "profile_form": profile_form,
        "breadcrumb_title": "User Management",
        "breadcrumbs": [
            {"name": "Categories", "url": reverse('user:user_list')},
            {"name": "Edit User"}
        ]
    }
    return render(request, 'user/form.html', context)

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    messages.success(request, "User deleted successfully.")

    return redirect('user:user_list')
