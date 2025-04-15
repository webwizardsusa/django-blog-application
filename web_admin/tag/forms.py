from django import forms
from .models import Tag

class TagForm(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tag name'}))

    class Meta:
        model = Tag
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        
        if not name:
            raise forms.ValidationError("Tag name is required.")   
        qs = Tag.objects.filter(name=name)

        # Exclude the current tag when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("Tag with this name already exists.")

        return name
