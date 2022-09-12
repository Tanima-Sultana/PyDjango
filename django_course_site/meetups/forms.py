from django import forms
from django.contrib.auth.models import User
from .models import Profile

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


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'phone_number',
            'birth_date',
            'profile_image'
        ]