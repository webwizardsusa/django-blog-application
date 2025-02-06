from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.http import JsonResponse
from .models import Category
from .forms import CategoryForm

def category_list(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        draw = int(request.GET.get('draw', 1))
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))
        search_value = request.GET.get('search[value]', '') 

        categories_query = Category.objects.all()
        if search_value:
            categories_query = categories_query.filter(name__icontains=search_value)
        total_records = Category.objects.count()
        filtered_records = categories_query.count()
        categories = categories_query[start:start + length]

        data = []
        for category in categories:
            category_data = {
                "name": category.name,
                "total_blogs": category.blogs.count(),
                "image": category.image.url if category.image else "",
                "created_at": category.created_at.strftime("%Y-%m-%d"),
                "actions": f"""
                    <a href='{reverse("category:category_edit", kwargs={"pk": category.id})}' class='btn btn-sm btn-warning'>Edit</a>
                    <a href='{reverse("category:category_delete", kwargs={"pk": category.id})}' class='btn btn-sm btn-danger' onclick='return confirm("Are you sure?");'>Delete</a>
                """
            }
            data.append(category_data)

        return JsonResponse({"draw": draw,  "recordsTotal": total_records, "recordsFiltered": filtered_records,  "data": data })

    return render(request, "list.html", {"breadcrumb_title": "Category Management","breadcrumbs": [{"name": "Categories"}]})

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
