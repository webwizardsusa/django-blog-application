from django import forms
from django.contrib.auth.models import User
import re


class AuthorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_active']
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter User Name title", 'required': True}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter First Name title", 'required': True}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Last Name title", 'required': True}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Email title", 'required': True}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Password", 'required': True}),
            "is_active": forms.Select(choices=[(1, 'Active'),(0, 'In Active')], attrs={"class": "form-control"}),
            # "user.groups": forms.HiddenInput(attrs={"class": "form-control",'value':2}),
        }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the password field optional
        self.fields['password'].required = False
        
    def clean_title(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        # Exclude the current User when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A Author with this title already exists.")
        
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get("password")

        # Check for minimum length
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")

        # Check for at least one uppercase letter
        if not any(char.isupper() for char in password):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")

        # Check for at least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise forms.ValidationError("Password must contain at least one special character (e.g., @, #, $, etc.).")

        return password
    

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)

        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A Author with this Email already exists.")
        return email
    
    
    
    
class AuthorUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_active']
        STATUS_CHOICES = {
    "0": "Inactive",
    "1": "Active",
}
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter User Name title", 'required': True}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter First Name title", 'required': True}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Last Name title", 'required': True}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Email title", 'required': True}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Password"}),
            "is_active": forms.Select(attrs={"class": "form-control"}, choices=[(False, 'Inactive'),(True, 'Active')]),
            # "user.groups": forms.HiddenInput(attrs={"class": "form-control",'value':2}),
        }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the password field optional
        self.fields['password'].required = False
        
    def clean_title(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        # Exclude the current User when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A Author with this title already exists.")
        
        return username
    

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)

        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A Author with this Email already exists.")
        return email