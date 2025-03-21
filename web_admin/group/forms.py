from django import forms
from django.contrib.auth.models import Group, Permission

class GroupForm(forms.ModelForm):
    excluded_models = ['logentry', 'permission', 'contenttype', 'session']
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.exclude(content_type__model__in=excluded_models),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False,
        label="Assign Permissions"
    )
    
    class Meta:
        model = Group
        fields = ['name', 'permissions']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Group Name', 'required':True}),
        }
