from dataclasses import fields
from django import forms
from home.models import  User
from django.forms import Textarea
from django.contrib.auth.models import User as UserDjango
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin


<<<<<<< HEAD
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
=======
from home.models import Avatar






class UserRegisterForm(UserCreationForm):
>>>>>>> 0dba04d436131733b5081eafe74e04fe290d9c9d

    username = forms.CharField(label="username", min_length=3)
    first_name = forms.CharField(label="Nombre", min_length=3)
    last_name = forms.CharField(label="Apellido", min_length=3)
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Password", widget=forms.PasswordInput)

<<<<<<< HEAD
    last_name = forms.CharField()
    first_name = forms.CharField() 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
    
        help_texts = {k:"" for k in fields}
=======
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class UserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
        ]
        widgets = {
            "email": forms.TextInput(attrs={"readonly": "readonly"}),
        }


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("image", )
>>>>>>> 0dba04d436131733b5081eafe74e04fe290d9c9d




