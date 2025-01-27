from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Tag
from .forms import TagForm

# Create your views here.
def tag_list(request):
    tags = Tag.objects.all()
    context = {
        "tags": tags,
        "breadcrumb_title": "Tag Management",
        "breadcrumbs": [
            {"name": "Tags"}
        ]
    }
    return render(request, 'tag/list.html', context)

def tag_create(request):
    form = TagForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Tag created successfully.")
            return redirect('tag:tag_list')

    context = {
        "form": form,
        "breadcrumb_title": "Tag Management",
        "breadcrumbs": [
            {"name": "Tags", "url": reverse('tag:tag_list')},
            {"name": "Create Tag"}
        ]
    }
    return render(request, 'tag/form.html', context)

def tag_edit(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    form = TagForm(request.POST or None, instance=tag)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Tag updated successfully.")
        return redirect("tag:tag_list")

    context = {
        "form": form,
        "tag": tag,
        "breadcrumb_title": "Tag Management",
        "breadcrumbs": [
            {"name": "Tags", "url": reverse('tag:tag_list')},
            {"name": "Edit Tag"}
        ]
    }
    
    return render(request, "tag/form.html", context)

def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tag.delete()
    messages.success(request, "Tag deleted successfully.")
    return redirect('tag:tag_list')