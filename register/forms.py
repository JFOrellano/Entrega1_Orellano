from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class PlayerForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "player-name",
                "placeholder": "Nombre",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "player-last_name",
                "placeholder": "Apellido",
                "required": "True",
            }
        ),
    )
    mail = forms.CharField(
        label="Email",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "team-name",
                "placeholder": "Mail",
                "required": "True",
            }
        ),
    )
    npassword = forms.IntegerField(
        label="Password",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "number-name",
                "placeholder": "Password",
                "required": "True",
            }
        ),
    )
    
    