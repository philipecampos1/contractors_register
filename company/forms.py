from django import forms
from . import models


class CompanyForm(forms.ModelForm):
    class Meta:
        model = models.Company
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'name': 'Company'
        }
