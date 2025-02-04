from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

class Crud:
    model = None
    module = None
    form = None 
    list_template_name = None
    list_url_name = None 
    form_url = None

    def list(self, request):
        results = self.model.objects.all()
        context = {
            "results": results,
            "breadcrumb_title": f"{self.model.__name__} Management",
            "breadcrumbs": [{"name": self.model.__name__}]
        }
        return render(request, self.list_template_name, context)
    
    def create(self, request):
        form = self.form(request.POST or None)

        if request.method == "POST" and form.is_valid():
            form.save()  
            messages.success(request, f"{self.model.__name__} created successfully.")
            return redirect(self.list_url_name)  

        context = {
            "form": form,
            "breadcrumb_title": f"{self.model.__name__} Management",
            "breadcrumbs": [
                {"name": f"{self.model.__name__}", "url": reverse(self.list_url_name)}, 
                {"name": f"Create {self.model.__name__}"}
            ]
        }
        return render(request, self.form_url, context)
    
    def edit(self, request, pk):
        self.module = self.model.__name__.lower()
        module_instance = get_object_or_404(self.model, pk=pk)
        form = self.form(request.POST or None, instance=module_instance)

        if request.method == "POST" and form.is_valid():
            form.save()
            messages.success(request, f"{self.model.__name__} updated successfully.")
            return redirect(self.list_url_name)  

        context = {
            "form": form,
            "module": module_instance,
            "breadcrumb_title": f"{self.model.__name__} Management",
            "breadcrumbs": [
                {"name":f"{self.model.__name__}", "url": reverse(self.list_url_name)},
                {"name": f"Edit {self.model.__name__}"}
            ]
        }
        
        return render(request, self.form_url, context)
    
    def delete(self, request, pk):
        self.module = self.model.__name__.lower()
        module_instance = get_object_or_404(self.model, pk=pk)

        module_instance.delete()
        messages.success(request, f"{self.model.__name__} deleted successfully.")
        return redirect(self.list_url_name)
