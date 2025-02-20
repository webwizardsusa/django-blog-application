from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from .models import Tag
from .forms import TagForm
from django.db.models import Count

# Create your views here.
def tag_list(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        draw = int(request.GET.get("draw", 1))  
        start = int(request.GET.get("start", 0))  
        length = int(request.GET.get("length", 10))  
        search_value = request.GET.get("search[value]", "").strip()  

        order_column_index = int(request.GET.get('order[0][column]', 0))
        order_dir = request.GET.get('order[0][dir]', 'desc')
    
        column_mapping = {
            0: "name",
            1: "total_blogs",
            2: "created_at",
        }
        
        order_column = column_mapping.get(order_column_index, "name")
        if order_dir == "desc":
            order_column = f"-{order_column}"

        tags = Tag.objects.annotate(total_blogs=Count("blogs"))
        tags = tags.order_by(order_column)
        
        if search_value:
            tags = tags.filter(name__icontains=search_value)
        records_total = tags.count()
        tags = tags[start:start+length]
        
        data = []
        for tag in tags:
            data.append({
                "name": tag.name, 
                "total_blogs": tag.blogs.count(), 
                "created_at": tag.created_at.strftime("%Y-%m-%d"), 
                "actions": f"""
                    <a href='{reverse("tag:tag_edit", kwargs={"pk": tag.id})}' class='btn btn-sm btn-warning'>Edit</a>
                    <a href='{reverse("tag:tag_delete", kwargs={"pk": tag.id})}' class='btn btn-sm btn-danger' onclick='return confirm("Are you sure?");'>Delete</a>
                """
            })

        return JsonResponse({"draw": draw, "recordsTotal": Tag.objects.count(), "recordsFiltered": records_total, "data": data}, safe=False)

    return render(request, "tag/list.html", {"breadcrumb_title": "Tag Management", "breadcrumbs": [{"name": "Tags"}]})

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
    # Check if the tag has any associated blogs
    if tag.blogs.exists():  # Using related_name='blogs' from the Blog model
        messages.error(request, "Cannot delete this tag because it has associated blogs.")

        return redirect("tag:tag_list")
    tag.delete()
    messages.success(request, "Tag deleted successfully.")
    return redirect('tag:tag_list')