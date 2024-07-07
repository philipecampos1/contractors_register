from django import forms
from . import models


class WorkTypeForm(forms.ModelForm):
    class Meta:
        model = models.WorkType
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'name': 'Work type'
        }
