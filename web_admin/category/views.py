from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Category
from .forms import CategoryForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'list.html', {'categories': categories})

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created successfully.")
            return redirect('category:category_list')
    else:
        form = CategoryForm()
    return render(request, 'form.html', {'form': form})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully.")
            return redirect('category:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, "Category deleted successfully.")
    return redirect('category:category_list')
