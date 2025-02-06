# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User, Group
from .forms import UserForm, UserUpdateForm, ProfileForm
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

def user_list(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        users = User.objects.filter(groups=2) 
        draw = int(request.GET.get('draw', 1)) 
        start = int(request.GET.get('start', 0))  
        length = int(request.GET.get('length', 10))  
        paginated_users = users[start:start+length]

        data = []
        for user in paginated_users:
            user_data = {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "status": f'<span class="badge bg-success">Active</span>' if user.is_active else f'<span class="badge bg-danger">In Active</span>',
                "edit_url": reverse("user:user_edit", kwargs={"pk": user.id}),
                "delete_url": reverse("user:user_delete", kwargs={"pk": user.id}),
            }
            data.append(user_data)

        return JsonResponse({"draw": draw, "recordsTotal": users.count(), "recordsFiltered": users.count(), "data": data,}, safe=False)
        
    return render(request, "user/list.html", {"breadcrumb_title": "Users Management","breadcrumbs": [{"name": "Users"}]})

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
