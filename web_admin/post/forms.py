from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'tags', 'image', 'content', 'is_published', 'author']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter post title"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "is_published": forms.Select(choices=Post.STATUS_CHOICES, attrs={"class": "form-control"}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply the filter for authors with a specific condition
        self.fields['author'].queryset = User.objects.filter(groups__id=2)
        
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        qs = Post.objects.filter(title=title)

        # Exclude the current post when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("A post with this title already exists.")
        
        return title
    
    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            return None  # Ensure None is returned if no image is uploaded
        return image
