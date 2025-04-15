from django import forms
from django.contrib.auth.models import Group, Permission

class GroupForm(forms.ModelForm):
    excluded_models = ['logentry', 'permission', 'contenttype', 'session']
    
    name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Group Name'}))
    
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.exclude(content_type__model__in=excluded_models),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False,
        label="Assign Permissions"
    )
    
    class Meta:
        model = Group
        fields = ['name', 'permissions']

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        
        if not name:
            raise forms.ValidationError("Group name is required.")
            
        qs = Group.objects.filter(name=name)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)  
        if qs.exists():
            raise forms.ValidationError("A group with this name already exists.") 
        return name
