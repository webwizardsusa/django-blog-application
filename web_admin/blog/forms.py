from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'image', 'content', 'is_published']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter blog title"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Enter blog content"}),
            "is_published": forms.Select(choices=Blog.STATUS_CHOICES, attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        qs = Blog.objects.filter(title=title)

        # Exclude the current blog when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("A blog with this title already exists.")
        
        return title
    
    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            return None  # Ensure None is returned if no image is uploaded
        return image
