from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Tag 
from .forms import TagForm
from web_admin.common.traits.crud import Crud

# Create your views here.
class TagCrud(Crud):
    model = Tag  
    form = TagForm 
    list_url = "tag/list.html"  
    redirect_url = "tag:tag_list"
    form_url = "tag/form.html" 
