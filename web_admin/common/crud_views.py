from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

class CrudView:
    module = None
    model = None
    form_class = None
    list_template_name = None
    form_template_name = None
    redirect_url = None

    def permission(self, request, action):
        if not request.user.has_perm(f"{self.model._meta.app_label}.{action}_{self.model._meta.model_name}"):
            messages.error(request, "You do not have permission to perform this action.")
            return redirect('web_admin_dashboard')
    

    def list(self, request):
        permission_check = self.permission(request, 'view')
        if permission_check:
            return permission_check 

        page = 'List'
        shared_data = (self._shareData(page, {'request': request}) or {}) if hasattr(self, '_shareData') else {}
        results = self._dataQuery(page)

        context = {'results': results} if results else {}
        self._pageHeader(page, context, shared_data)
        context.update(shared_data)

        return render(request, self.list_template_name, context)
    
    def datatable(self, request):
        _dt = self._dt()
        sort_fields = _dt['sort']
        search_fields = _dt['search']
        select_fields = _dt['select']
        query = _dt['query']

        data = []
       
        if hasattr(self, "_filter"):
            query = self._filter(query, request)

        search = request.POST.get('search[value]', '').strip()
        order_column = int(request.POST.get('order[0][column]', 0)) 
        order_dir = request.POST.get('order[0][dir]', 'asc') 
        start = int(request.POST.get('start', 0))
        length = int(request.POST.get('length', 10))

        sort_column = sort_fields[order_column]

        total_rows = query.count()

        if search and search_fields:
            search_query = Q()
            for field in search_fields:
                search_query |= Q(**{field: search})
            query = query.filter(search_query)

        total_filtered_rows = query.count()

        if order_dir == 'asc':
            query = query.order_by(sort_column)
        else:
            query = query.order_by(f'-{sort_column}')
        
        query = query[start:start + length]

        data = list(query.values(*select_fields))

        return JsonResponse({
            'draw': int(request.POST.get('draw', 1)),
            'recordsTotal': total_rows,  
            'recordsFiltered': total_filtered_rows, 
            'data': data
        })

    def form(self, request, id = None):
        permission_check = self.permission(request, 'add' if id is None else 'change')
        if permission_check:
            return permission_check 
        
        if id == None:
            page, message, instance = 'Create', f"{self.module} created successfully!", None
        else:
            try:
                page, message, instance = 'Edit', f"{self.module} updated successfully!", self._dataQuery('Edit', id=id)
            except self.model.DoesNotExist:
                messages.error(request, f"{self.module} not found!")
                return redirect(self.redirect_url)

        post_data = request.POST.copy() if request.method == 'POST' else None
        params = {'request': request, 'post_data': post_data, 'instance': instance, 'id': id}
        shared_data = (self._shareData(page, params) or {}) if hasattr(self, '_shareData') else {}
        
        if request.method == 'POST':
            if hasattr(self, '_beforeSave'):
                post_data = self._beforeSave(params)

            form = self.form_class(data=post_data, files=request.FILES, instance=instance)
            params.update({'form': form, **shared_data})
            form_save = False

            if hasattr(self, '_save'):
                form_save = self._save(params)
            else:
                if form.is_valid():
                    if hasattr(self, '_afterSave'):
                        after_save = form.save(commit=False)

                        params.update({'form_save': after_save})
                        form_save = self._afterSave(params)
                    else:
                        form_save = form.save()

            if form_save:
                messages.success(request, message)
                return redirect(self.redirect_url)
        else:       
            form = self.form_class(instance=instance)

        context = {'form': form, 'page': page}
        self._pageHeader(page, context, shared_data)
        context.update(shared_data)

        return render(request, self.form_template_name, context)

    def delete(self, request, id):
        permission_check = self.permission(request, 'delete')
        if permission_check:
            return permission_check 
            
        if request.method == 'POST':
            page = 'Delete'

            try:
                result = self._dataQuery(page, id=id)
            except self.model.DoesNotExist:
                messages.error(request, f"{self.module} not found!")
                return redirect(self.redirect_url)

            result.delete()
            messages.success(request, f"{self.module} deleted successfully!")
            return redirect(self.redirect_url)

    def _dataQuery(self, page, id = None):
        query = None

        if hasattr(self, '_query'):
            query = self._query(page, id) or {}

        if not query and page in ('Edit', 'Delete'):
            query = self.model.objects.get(id=id)
        
        return query
        
    def _pageHeader(self, page, context, shared_data={}):
        if page == 'List':
            context['title'] = shared_data.get('title', f"{self.module}s")
            context['breadcrumb'] = shared_data.get('breadcrumb', [{'text': f"{self.module}s List"}])
        elif page in ('Create', 'Edit'):
            context['title'] = shared_data.get('title', f"{page} {self.module}")
            context['breadcrumb'] = shared_data.get('breadcrumb', [
                {'url': self.redirect_url, 'text': f"{self.module}s"}, 
                {'text': f"{page} {self.module}"}
            ])
        
        return context
    