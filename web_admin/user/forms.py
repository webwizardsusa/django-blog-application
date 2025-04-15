from django import forms
from django.contrib.auth.models import User
from .models import Profile
import re

class UserForm(forms.ModelForm):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter User Name"}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter First Name"}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Last Name"}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email"}))
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Password"}))
    is_active = forms.ChoiceField(required=False,choices=[(1, 'Active'), (0, 'In Active')], widget=forms.Select(attrs={"class": "form-control"}), initial=1)
    groups = forms.ModelMultipleChoiceField(required=False,queryset=None, widget=forms.SelectMultiple(attrs={"class": "form-control"}))
    image = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter author description", "rows": 5}), required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'groups', 'password', 'is_active']
        use_required_attribute = False 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['groups'].queryset = User._meta.get_field('groups').remote_field.model.objects.all()
        if self.instance.pk:
            profile = Profile.objects.filter(user=self.instance).first()
            if profile:
                self.fields['image'].initial = profile.image
                self.fields['description'].initial = profile.description

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("Username is required.")
            
        qs = User.objects.filter(username=username)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A User with this username already exists.")
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("First name is required.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError("Last name is required.")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("Email is required.")
            
        qs = User.objects.filter(email=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A User with this Email already exists.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if self.instance.pk and not password:
            return ''  
        if not self.instance.pk and not password:
            raise forms.ValidationError("Password is required for new users.")
        if password:
            if len(password) < 8:
                raise forms.ValidationError("Password must be at least 8 characters long.")
            if not any(char.isupper() for char in password):
                raise forms.ValidationError("Password must contain at least one uppercase letter.")
            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                raise forms.ValidationError("Password must contain at least one special character (e.g., @, #, $, etc.).")
        return password

    def clean_groups(self):
        groups = self.cleaned_data.get('groups')
        if not groups:
            raise forms.ValidationError("At least one group must be selected.")
        return groups

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get('password'):
            user.set_password(self.cleaned_data['password'])
        elif not self.instance.pk:
            user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

            if self.cleaned_data.get("groups"):
                user.groups.set(self.cleaned_data["groups"]) 

            profile, _ = Profile.objects.update_or_create(user=user,defaults={"image": self.cleaned_data.get("image"), "description": self.cleaned_data.get("description"),})
        return user