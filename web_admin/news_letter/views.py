from django.shortcuts import render, redirect
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
            print('Yes1') 
            news_letter = form.save(commit=False)
            news_letter.user = request.user
            print('Correct1')
            news_letter.save()
            messages.success(request, "News Letter created successfully.")
            return redirect('news_letter:news_letters_list')

    context = {
        "form": form,
        "breadcrumb_title": "News Letter Management",
        "breadcrumbs": [
            {"name": "News Letters", "url": reverse('news_letter:news_letters_list')},
            {"name": "Create Blog"}
        ]
    }
    return render(request, 'news_letters/form.html', context)