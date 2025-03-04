from django import forms
from .models import Contact
from django.core.exceptions import ValidationError
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone', 'email', 'subject', 'message']
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none", "placeholder": "Enter First Name"}),
            "last_name": forms.TextInput(attrs={"class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none", "placeholder": "Enter Last Name"}),
            "email": forms.EmailInput(attrs={"class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none", "placeholder": "Enter Your Email"}),
            "phone": forms.TextInput(attrs={"class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none", "placeholder": "Enter Phone Number"}),
            "subject": forms.TextInput(attrs={"class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none", "placeholder": "Enter Subject"}),
            "message": forms.Textarea(attrs={"class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none", "rows": 5, "placeholder": "Enter Message"}),
        }
        
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError("Phone number should contain only digits.")
        if len(phone) < 10 or len(phone) > 15:
            raise forms.ValidationError("Phone number must be between 10 and 15 digits.")
        return phone
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if re.search(r'\d', first_name):
            raise forms.ValidationError("First Name should contain only Alphabetic.")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if re.search(r'\d', last_name):
            raise forms.ValidationError("Last Name should contain only Alphabetic.")
        return last_name
    
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 100:
            raise forms.ValidationError("Please write message minimum 100 characters")
        return message
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        return email