from django import forms
from .models import OrientationRequest


class OrientationRequestForm(forms.ModelForm):
    class Meta:
        model = OrientationRequest
        fields = "__all__"

        widgets = {
            "date": forms.DateInput(
                attrs={
                    "class": "w3-input w3-padding-16",
                    "id": "id_date",
                    "name": "date",
                }
            ),
        }

    time = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w3-input w3-padding-16",
                "id": "id_time",
                "type": "text",
                "required": True,
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w3-input w3-padding-16",
                "placeholder": "First name...",
                "type": "text",
                "required": True,
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w3-input w3-padding-16",
                "placeholder": "Last name...",
                "type": "text",
                "required": True,
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "w3-input w3-padding-16",
                "placeholder": "E-mail...",
                "type": "email",
                "required": True,
            }
        )
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w3-input w3-padding-16",
                "placeholder": "Phone...",
                "type": "tel",
                "required": True,
            }
        )
    )
