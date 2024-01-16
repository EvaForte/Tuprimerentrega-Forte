from django import forms

from . import models


class CoordinadorForm(forms.ModelForm):
    class Meta:
        model = models.Coordinador
        fields = ["nombre", "email"]
