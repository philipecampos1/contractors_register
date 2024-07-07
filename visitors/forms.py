from django import forms
from . import models


class VisitorForm(forms.ModelForm):
    class Meta:
        model = models.Visitor
        fields = ['name', 'staircase', 'telephone_number', 'arriving_time', 'leaving_time', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'staircase': forms.Select(attrs={'class': 'form-control'}),
            'telephone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'arriving_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'leaving_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

        }

        lables = {
            'name': 'Name',
            'staircase': 'Staircase',
            'telephone_number': 'Telephone number',
            'arriving_time': 'Arriving time',
            'leaving_time': 'Leaving time',
            'is_active': 'In the building',
        }
