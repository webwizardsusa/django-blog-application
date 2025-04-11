from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True,
        widget=forms.TextInput(
            attrs={'class': 'mt-1 block w-full px-4 py-3 bg-white border border-gray-300 rounded-md text-sm shadow-sm placeholder-gray-400 focus:outline-none focus:border-red-500 focus:ring-1 focus:ring-red-500', 'placeholder': 'Enter your Username', 'required': False, }),
        error_messages={
            'required': 'Username is required',
        }
    )
    password = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={'class': 'mt-1 block w-full px-4 py-3 bg-white border border-gray-300 rounded-md text-sm shadow-sm placeholder-gray-400 focus:outline-none focus:border-red-500 focus:ring-1 focus:ring-red-500', 'placeholder': 'Enter your password', 'id': 'id_password_field', 'required': False,  }),
        error_messages={
            'required': 'Password is required',
        }
    )
    remember_me = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(attrs={'class': 'h-4 w-4 text-red-600 focus:ring-red-500 border-gray-300 rounded',})
    )

    error_messages = {
        'invalid_login': 'Please enter a correct username and password. Note that both fields may be case-sensitive.',
        'inactive': 'This account is inactive.',
    }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            cleaned_data['username'] = username.lower()

        return cleaned_data

class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'class': 'mt-1 block w-full px-4 py-3 bg-white border border-gray-300 rounded-md text-sm shadow-sm placeholder-gray-400 focus:outline-none focus:border-red-500 focus:ring-1 focus:ring-red-500', 'placeholder': 'Enter your username', 'required': False, }),
        error_messages={
            'required': 'Username is required',
            'unique': 'This username is already taken.',
        }
    )
    email = forms.EmailField(required=True,
        widget=forms.EmailInput(attrs={'class': 'mt-1 block w-full px-4 py-3 bg-white border border-gray-300 rounded-md text-sm shadow-sm placeholder-gray-400 focus:outline-none focus:border-red-500 focus:ring-1 focus:ring-red-500', 'placeholder': 'Enter your email address', 'required': False,}),
        error_messages={
            'required': 'Email address is required',
            'invalid': 'Please enter a valid email address',
        }
    )   
    password1 = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={'class': 'mt-1 block w-full px-4 py-3 bg-white border border-gray-300 rounded-md text-sm shadow-sm placeholder-gray-400 focus:outline-none focus:border-red-500 focus:ring-1 focus:ring-red-500', 'placeholder': 'Enter your password', 'id': 'id_password1','required': False,}),
        error_messages={
            'required': 'Password is required',
        }
    )
    password2 = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={'class': 'mt-1 block w-full px-4 py-3 bg-white border border-gray-300 rounded-md text-sm shadow-sm placeholder-gray-400 focus:outline-none focus:border-red-500 focus:ring-1 focus:ring-red-500', 'placeholder': 'Confirm your password', 'id': 'id_password2', 'required': False, }),
        error_messages={
            'required': 'Please confirm your password',
        }
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already registered.')
        return email
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username.lower()

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and len(password1) < 8:
            self.add_error('password1', 'Password must be at least 8 characters long.')
        
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Passwords do not match.') 

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(required=True, 
    widget=forms.EmailInput(attrs={'class': 'mt-1 block w-full px-4 py-3 bg-white border border-gray-300 rounded-md text-sm shadow-sm placeholder-gray-400 focus:outline-none focus:border-red-500 focus:ring-1 focus:ring-red-500', 'placeholder': 'Enter your email address', 'required': False, }),
        error_messages={
            'required': 'Email address is required',
            'invalid': 'Please enter a valid email address',
        }
    )