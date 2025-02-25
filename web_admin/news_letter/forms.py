from django import forms
from .models import NewsLetter
from django.contrib.auth.models import Group
from ckeditor.widgets import CKEditorWidget

class NewsLetterForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetter
        fields = ['title', 'subject', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter News Letter title'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter News Letter subject'}),
            'content': forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control', 'rows': 20})),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) < 5:
            raise forms.ValidationError("Given title is too short.")
        
        return title