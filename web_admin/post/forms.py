from django import forms
from .models import Post
from django.contrib.auth.models import User
from web_admin.category.models import Category
from web_admin.tag.models import Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'tags', 'image', 'content', 'is_published', 'author']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter post title"}),
            "category": forms.Select(attrs={"class": "form-control", "id": "id_category"}),
            "author": forms.Select(attrs={"class": "form-control", "id": "id_author"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-control", "id": "id_tag", "data-placeholder": "Select or enter new tags", "required": True}),
            "is_published": forms.Select(choices=Post.STATUS_CHOICES, attrs={"class": "form-control"}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply the filter for authors with a specific condition
        self.fields['author'].queryset = User.objects.filter(groups__name="author")
        
        
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

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        tag_objects = []
        
        for tag in tags:
            if isinstance(tag, str):
                # This is a new tag
                tag_obj, created = Tag.objects.get_or_create(name=tag)
                tag_objects.append(tag_obj)
            else:
                tag_objects.append(tag)
                
        return tag_objects

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        author = cleaned_data.get('author')
        tags = cleaned_data.get('tags')

        if not category:
            self.add_error('category', 'Category is required.')
        if not author:
            self.add_error('author', 'Author is required.')
        if not tags:
            self.add_error('tags', 'At least one tag is required.')

        return cleaned_data


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]