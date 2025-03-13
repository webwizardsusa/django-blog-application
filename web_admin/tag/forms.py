from django import forms
from .models import Tag

class TagForm(forms.ModelForm):
    name = forms.CharField(required=True)

    class Meta:
        model = Tag
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        qs = Tag.objects.filter(name=name)

        # Exclude the current tag when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("Tag with this name already exists.")

        return name
