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
    team = forms.CharField(
        label="Equipo",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "team-name",
                "placeholder": "Equipo",
                "required": "True",
            }
        ),
    )
    number = forms.IntegerField(
        label="Número",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "number-name",
                "placeholder": "Número",
                "required": "True",
            }
        ),
    )
    position = forms.CharField(
        label="Posición",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "position-name",
                "placeholder": "Posición",
                "required": "True",
            }
        ),
    )
    