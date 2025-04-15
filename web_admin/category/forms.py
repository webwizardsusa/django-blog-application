from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 4}))
    image = forms.ImageField(required=False)

    class Meta:
        model = Category
        fields = ['name', 'image', 'description']

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        
        if not name:
            raise forms.ValidationError("Category name is required.")
                    
        qs = Category.objects.filter(name=name)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Category with this name already exists.")

        return name
    
    def clean_description(self):
        description = self.cleaned_data.get('description', '').strip()
        
        if not description:
            raise forms.ValidationError("Category description is required.")
        return description
    
    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            return None  # Ensure None is returned if no image is uploaded
        return image
