from django import forms
from .models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tag name'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        qs = Tag.objects.filter(name=name)

        # Exclude the current tag when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("Tag with this name already exists.")

        return name
