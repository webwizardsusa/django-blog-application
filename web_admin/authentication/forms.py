from django import forms
from django.contrib.auth.forms import PasswordResetForm

class AdminPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }
        )
    ) 