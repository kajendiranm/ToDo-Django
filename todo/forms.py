from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PasswordInputWithPlaceholder(forms.PasswordInput):
    def __init__(self, attrs=None, placeholder=None):
        super().__init__(attrs)
        if placeholder:
            self.attrs['placeholder'] = placeholder

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        widgets = {
            'username':forms.TextInput(attrs={'placeholder': 'Username'}),
            'email':forms.EmailInput(attrs={'placeholder':'Email'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20,
                               widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'custom-password-input','placeholder':'Password'}),
    )
