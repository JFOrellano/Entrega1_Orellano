from dataclasses import fields
from django import forms
from home.models import  User
from django.forms import Textarea
from django.contrib.auth.models import User as UserDjango
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin









class UserRegisterForm(UserCreationForm):
    username = forms.EmailField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    last_name = forms.CharField()
    first_name = forms.CharField()
class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
 
    help_texts = {k:"" for k in fields}

class UserEditrForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField() 
class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
 
    help_texts = {k:"" for k in fields}




