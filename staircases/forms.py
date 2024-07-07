from django import forms
from . import models


class StaircaseForm(forms.ModelForm):
    class Meta:
        model = models.Staircase
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'name': 'Staircase'
        }
