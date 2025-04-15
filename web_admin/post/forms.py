from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter post title"}))
    category = forms.ModelChoiceField(required=False, queryset=None, widget=forms.Select(attrs={"class": "form-control"}))
    tags = forms.ModelMultipleChoiceField(required=False, queryset=None, widget=forms.SelectMultiple(attrs={"class": "form-control"}))
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
    author = forms.ModelChoiceField(required=False, queryset=None, widget=forms.Select(attrs={"class": "form-control"}))
    is_published = forms.ChoiceField(required=False, choices=Post.STATUS_CHOICES, widget=forms.Select(attrs={"class": "form-control"}),initial=Post.PUBLISHED)
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'category', 'tags', 'image', 'content', 'is_published', 'author']
        use_required_attribute = False  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = User.objects.filter(groups__id=2)
        self.fields['category'].queryset = Post._meta.get_field('category').remote_field.model.objects.all()
        self.fields['tags'].queryset = Post._meta.get_field('tags').remote_field.model.objects.all()
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title is required.")
            
        qs = Post.objects.filter(title=title)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A post with this title already exists.")
        return title
    
    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError("Category is required.")
        return category
    
    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if not tags:
            raise forms.ValidationError("At least one tag is required.")
        return tags
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Content is required.")
        return content
    
    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author:
            raise forms.ValidationError("Author is required.")
        return author
    
    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            return None
        return image
