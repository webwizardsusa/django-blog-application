# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User, Group
from .forms import AuthorForm, AuthorUpdateForm
from django.http import HttpResponse
from django.contrib import messages

def author_list(request):
    authors = User.objects.all().filter(groups=2)
    context = {
        "authors": authors,
        "breadcrumb_title": "Authors",
        "breadcrumbs": [
            {"name": "Authors"}
        ]
    }

    return render(request, 'author/list.html', {'context':context})

def author_create(request):
    form = AuthorForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            group = Group.objects.get(id=2)
            group.user_set.add(author)  
            messages.success(request, "Author created successfully.")
            return redirect('author:author_list')
    else:
        form = AuthorForm()

    context = {
        "form": form,
        "breadcrumb_title": "Author Management",
        "breadcrumbs": [
            {"name": "Authors", "url": reverse('author:author_list')},
            {"name": "Create Author"}
        ]
    }
    return render(request, 'author/form.html', context)

def author_edit(request, pk):
    author = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = AuthorUpdateForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, "Author updated successfully.")
            return redirect('author:author_list')
    else:
        form = AuthorUpdateForm(instance=author)

    context = {
        "form": form,
        "breadcrumb_title": "Author Management",
        "breadcrumbs": [
            {"name": "Categories", "url": reverse('author:author_list')},
            {"name": "Edit Author"}
        ]
    }
    return render(request, 'author/form.html', context)

def author_delete(request, pk):
    author = get_object_or_404(User, pk=pk)
    author.delete()
    messages.success(request, "Author deleted successfully.")

    return redirect('author:author_list')
