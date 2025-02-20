from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email' : forms.EmailInput(attrs={'class': 'h-14 w-full rounded-3xl border-0 border-transparent bg-white py-3.5 pl-6 pr-36 text-sm leading-5 text-gray-800 transition duration-300 ease-in-out hover:bg-transparent focus:bg-white focus:outline-none focus:ring-2 focus:ring-red-100', 'placeholder':'Please enter your email', 'autocomplete':'email'}),
        }
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = Subscriber.objects.filter(email=email)

        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("This Email already exists.")
        return email
            