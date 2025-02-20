from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.http import JsonResponse
from .models import Category
from .forms import CategoryForm
from django.db.models import Count

def category_list(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        draw = int(request.GET.get('draw', 1))
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))
        search_value = request.GET.get('search[value]', '') 

        order_column_index = int(request.GET.get('order[0][column]', 0))
        order_dir = request.GET.get('order[0][dir]', 'desc')
    
        column_mapping = {
            0: "name",
            1: "total_blogs",
            2: "image",
            2: "created_at"
        }
        
        order_column = column_mapping.get(order_column_index, "title")
        if order_dir == "desc":
            order_column = f"-{order_column}"
            
        categories = Category.objects.annotate(total_blogs=Count("blogs"))
        categories = categories.order_by(order_column)
        if search_value:
            categories = categories.filter(name__icontains=search_value)
        records_total = categories.count()
        categories = categories[start:start + length]

        data = []
        for category in categories:
            data.append({
                "name": category.name,
                "total_blogs": category.blogs.count(),
                "image": category.image.url if category.image else "",
                "created_at": category.created_at.strftime("%Y-%m-%d"),
                "actions": f"""
                    <a href='{reverse("category:category_edit", kwargs={"pk": category.id})}' class='btn btn-sm btn-warning'>Edit</a>
                    <a href='{reverse("category:category_delete", kwargs={"pk": category.id})}' class='btn btn-sm btn-danger' onclick='return confirm("Are you sure?");'>Delete</a>
                """
            })
           
        return JsonResponse({"draw": draw,  "recordsTotal": Category.objects.count(), "recordsFiltered": records_total, "data": data}, safe=False)

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
