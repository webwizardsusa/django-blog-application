from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 4}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        qs = Category.objects.filter(name=name)

        # Exclude the current category when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("Category with this name already exists.")

        return name
    
    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            return None  # Ensure None is returned if no image is uploaded
        return image
