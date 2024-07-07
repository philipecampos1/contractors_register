from django import forms
from . import models


class WorkerForm(forms.ModelForm):
    class Meta:
        model = models.Worker
        fields = ['name', 'staircase', 'telephone_number', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter worker name'
            }),
            'staircase': forms.Select(attrs={
                'class': 'form-control',
            }),
            'telephone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter telephone number',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            })

        }

        labels = {
            'name': 'Name',
            'staircase': 'Staircase',
            'telephone_number': 'Telephone number',
            'email': 'Email'
        }
