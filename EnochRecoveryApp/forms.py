from django import forms
from .models import OrientationRequest


class CustomerForm(forms.ModelForm):
    class Meta:
        model = OrientationRequest
        fields = "__all__"
