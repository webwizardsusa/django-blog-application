from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Category
from .forms import CategoryForm

def category_list(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "breadcrumb_title": "Category Management",
        "breadcrumbs": [
            {"name": "Categories"}
        ]
    }
    return render(request, 'list.html', context)

def category_create(request):
    form = CategoryForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Category created successfully.")
            return redirect('category:category_list')

    context = {
        "form": form,
        "breadcrumb_title": "Category Management",
        "breadcrumbs": [
            {"name": "Categories", "url": reverse('category:category_list')},
            {"name": "Create Category"}
        ]
    }
    return render(request, 'form.html', context)

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, request.FILES or None, instance=category)

    if request.method == "POST" and form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully.")
            return redirect('category:category_list')

    context = {
        "form": form,
        "breadcrumb_title": "Category Management",
        "breadcrumbs": [
            {"name": "Categories", "url": reverse('category:category_list')},
            {"name": "Edit Category"}
        ]
    }
    return render(request, 'form.html', context)

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    # Check if the category has any associated blogs
    if category.blogs.exists():  # Using related_name='blogs' from the Blog model
        messages.error(request, "Cannot delete this category because it has associated blogs.")

        return redirect("category:category_list")
    
    category.delete()
    messages.success(request, "Category deleted successfully.")

    return redirect('category:category_list')
