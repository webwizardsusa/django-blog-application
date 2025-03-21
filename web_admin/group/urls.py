from django.urls import path
from .views import GroupView

app_name = 'group' 

urlpatterns =[
    path('', GroupView().list, name='group_list'),
    path('create/', GroupView().form, name='group_create'),
    path('<int:id>/edit/', GroupView().form, name='group_edit'),
    path('<int:id>/delete/', GroupView().delete, name='group_delete'),
    path("datatable", GroupView().datatable, name="group_datatable"),
]