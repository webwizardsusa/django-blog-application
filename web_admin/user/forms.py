from django import forms
from django.contrib.auth.models import User
from .models import Profile
import re

class UserForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter author description", "rows": 5}),
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'groups' ,'password', 'is_active']
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter User Name title", 'required': True}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter First Name title", 'required': True}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Last Name title", 'required': True}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Email title", 'required': True}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Password", 'required': True}),
            "is_active": forms.Select(choices=[(1, 'Active'),(0, 'In Active')], attrs={"class": "form-control"}),
            "groups": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            profile = Profile.objects.filter(user=self.instance).first()
            if profile:
                self.fields['image'].initial = profile.image
                self.fields['description'].initial = profile.description
        self.fields['password'].required = False
        
    def clean_title(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        # Exclude the current User when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A User with this title already exists.")
        
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
            raise forms.ValidationError("A User with this Email already exists.")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

            if self.cleaned_data.get("groups"):
                user.groups.set(self.cleaned_data["groups"]) 

            profile, _ = Profile.objects.update_or_create(
                user=user,
                defaults={
                    "image": self.cleaned_data.get("image"),
                    "description": self.cleaned_data.get("description"),
                }
            )

        return user