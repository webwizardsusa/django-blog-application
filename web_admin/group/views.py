from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group, User
from django.urls import reverse
from .forms import GroupForm
from django.http import JsonResponse
from django.contrib import messages

def group_list(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        draw = int(request.GET.get('draw', 1))
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))
        search_value = request.GET.get("search[value]", "").strip()  

        order_column_index = int(request.GET.get('order[0][column]', 0)) 
        order_dir = request.GET.get('order[0][dir]', 'asc')

        column_mapping = {
            0: "name",
        }

        order_column = column_mapping.get(order_column_index, "name")
        if order_dir == "desc":
            order_column = f"-{order_column}"
        groups = Group.objects.all().order_by(order_column)

        if search_value:
            groups = groups.filter(name__icontains=search_value)

        records_total = Group.objects.count()
        records_filtered = groups.count()
        groups = groups[start:start + length]

        data = []
        for group in groups:
            data.append({
                "name": group.name,
                "actions": f"""
                    <a href='{reverse("group:group_edit", kwargs={"pk": group.id})}' class='btn btn-sm btn-warning'>Edit</a>
                    <a href='{reverse("group:group_delete", kwargs={"pk": group.id})}' class='btn btn-sm btn-danger' onclick='return confirm("Are you sure?");'>Delete</a>
                """
            })

        return JsonResponse({"draw": draw, "recordsTotal": records_total, "recordsFiltered": records_filtered, "data": data}, safe=False)

    return render(request, "group/list.html", {"breadcrumb_title": "Group Management", "breadcrumbs": [{"name": "Groups"}]})


def group_create(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            form.save_m2m()
            messages.success(request, "Groups created successfully.")
            return redirect("group:group_list")  
    else:
        form = GroupForm()

    context = {"form": form, "breadcrumb_title": "Group Management",
        "breadcrumbs": [
            {"name": "Groups", "url": reverse('group:group_list')},
            {"name": "Create Group"}
        ]
    }
    return render(request, "group/form.html", context)

def group_edit(request, pk):
    groups = get_object_or_404(Group, pk=pk)
    form = GroupForm(request.POST or None, request.FILES or None, instance=groups)

    if request.method == "POST" and form.is_valid():
            group_instance = form.save(commit=False)  
            group_instance.save()  
            form.save_m2m() 
            
            messages.success(request, "Group updated successfully.")
            return redirect('group:group_list')

    context = {"form": form, "groups": groups, "breadcrumb_title": "Group Management",
        "breadcrumbs": [
            {"name": "Groups", "url": reverse('group:group_list')},
            {"name": "Edit Group"}
        ]
    }
    return render(request, 'group/form.html', context)

def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if User.objects.filter(groups=group).exists():  
        messages.error(request, "Cannot delete this group because it has associated users.")
        return redirect("group:group_list")

    group.delete()
    messages.success(request, "Group deleted successfully.")
    return redirect("group:group_list")