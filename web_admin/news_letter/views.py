from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import NewsLetter
from .forms import NewsLetterForm
from django.contrib import messages

# Create your views here.
def news_letters_list(request):
    news_letters = NewsLetter.objects.all()
    context = {
        "news_letters": news_letters,
        "breadcrumb_title": "News Letters",
        "breadcrumbs": [
            {"name": "News Letters"}
        ]
    }

    return render(request, 'news_letters/list.html', context)

def news_letter_create(request):
    form = NewsLetterForm(request.POST or None) 
            
    if request.method == "POST":
        if form.is_valid():
            news_letter = form.save(commit=False)
            news_letter.user = request.user
            news_letter.save()
            messages.success(request, "News Letter created successfully.")
            return redirect('news_letter:news_letters_list')

    context = {
        "form": form,
        "breadcrumb_title": "News Letter Management",
        "breadcrumbs": [
            {"name": "News Letters", "url": reverse('news_letter:news_letters_list')},
            {"name": "Create New Letter"}
        ]
    }
    return render(request, 'news_letters/form.html', context)


def news_letter_edit(request, pk):
    news_letter = get_object_or_404(NewsLetter, pk=pk)
    form = NewsLetterForm(request.POST or None, request.FILES or None, instance=news_letter)
            
    if request.method == "POST" and form.is_valid():
        if form.is_valid():
            print('Yes1') 
            news_letter = form.save(commit=False)
            news_letter.user = request.user
            news_letter.save()
            messages.success(request, "News Letter updated successfully.")
            return redirect('news_letter:news_letters_list')

    context = {
        "form": form,
        "breadcrumb_title": "News Letter Management",
        "breadcrumbs": [
            {"name": "News Letters", "url": reverse('news_letter:news_letters_list')},
            {"name": "Edit News Letter"}
        ]
    }
    return render(request, 'news_letters/form.html', context)


def news_letter_delete(request, pk):
    news_letter = get_object_or_404(NewsLetter, pk=pk)
    news_letter.delete()
    messages.success(request, "News Letter deleted successfully.")
    return redirect('news_letter:news_letters_list')