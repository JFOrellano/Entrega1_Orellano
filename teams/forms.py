from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class TeamForm(forms.Form):
    name = forms.CharField(
        label="Nombre del equipo",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "team-name",
                "placeholder": "Nombre del equipo",
                "required": "True",
            }
        ),
    )
    federation = forms.CharField(
        label="Federacion de pertenencia",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "federation-name",
                "placeholder": "Federacion de pertenencia",
                "required": "True",
            }
        ),
    )
    country = forms.CharField(
        label="Pais de origen",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "country-name",
                "placeholder": "Pais de origen",
                "required": "True",
            }
        ),
    )
    city = forms.CharField(
        label="Ciudad",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "country-name",
                "placeholder": "Ciudad",
                "required": "True",
            }
        ),
    )
    fundation_date = forms.DateField(label='Release year', required=False, widget=AdminDateWidget
    )
    