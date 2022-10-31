from django import forms


class FederationForm(forms.Form):
    name = forms.CharField(
        label="Nombre de la federación",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "course-name",
                "placeholder": "Nombre de la federación",
                "required": "True",
            }
        ),
    )
    initials = forms.CharField(
        label="Sigla de la federación",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "course-name",
                "placeholder": "Sigla de la federación",
                "required": "True",
            }
        ),
    )
    official_website = forms.CharField(
        label="Sitio oficial",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "course-name",
                "placeholder": "Sitio oficial",
                "required": "True",
            }
        ),
    )
    