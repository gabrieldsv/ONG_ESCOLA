from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)