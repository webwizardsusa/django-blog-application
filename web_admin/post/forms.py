from django import forms
from .models import Post
from django.contrib.auth.models import User
from web_admin.category.models import Category
from web_admin.tag.models import Tag

class PostForm(forms.ModelForm):
    title = forms.CharField(required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, widget=forms.Select(attrs={"class": "form-control"}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=forms.SelectMultiple(attrs={"class": "form-control"}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter post content"}))
    author = forms.ModelChoiceField(queryset=User.objects.filter(groups__id=2), required=False, widget=forms.Select(attrs={"class": "form-control"}))
    is_published = forms.ChoiceField(choices=Post.STATUS_CHOICES, required=False, widget=forms.Select(attrs={"class": "form-control"}), initial=Post.PUBLISHED)

    class Meta:
        model = Post
        fields = ['title', 'category', 'tags', 'image', 'content', 'is_published', 'author']    

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

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError("This field is required.")  
        return category
    
    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if not tags:
            raise forms.ValidationError("This field is required.")  
        return tags
    
    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author:
            raise forms.ValidationError("This field is required.")  
        return author
