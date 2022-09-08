from django import forms
from .models import Participant

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email',help_text='Enter here',widget=forms.EmailInput )
    # password = forms.CharField(widget=forms.PasswordInput,label="Enter your password")

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password


class Subscribe(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email