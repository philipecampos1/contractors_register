from django import forms
from . import models


class ContractorForm(forms.ModelForm):
    class Meta:
        model = models.Contractor
        fields = ['work_type', 'company', 'work_code', 'work_reason', 'responsible_worker',
                  'contractor_name', 'contractor_number', 'expected_arriving_time',
                  'arriving_time', 'leaving_time', 'staircase',
                  'location', 'in_the_building', 'is_active']
        widgets = {
            'work_type': forms.Select(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'work_code': forms.TextInput(attrs={'class': 'form-control'}),
            'work_reason': forms.TextInput(attrs={'class': 'form-control'}),
            'responsible_worker': forms.Select(attrs={'class': 'form-control'}),
            'contractor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contractor_number': forms.TextInput(attrs={'class': 'form-control'}),
            'staircase': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'expected_arriving_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'arriving_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'leaving_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'in_the_building': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        labels = {
            'work_type': 'Type of work',
            'company': 'Company name',
            'work_code': 'Work code',
            'responsible_worker': 'Host',
            'contractor_name': 'Name of the contractor',
            'contractor_number': 'Number of the contractor',
            'staircase': 'Staircase',
            'location': 'Where the contractor will be working',
            'expected_arriving_time': 'When to expect the contractor',
            'arriving_time': 'When the contractor has arrive',
            'leaving_time': 'When the contractor has left',
            'in_the_building': 'If the contractor is in the building',
            'is_active': 'If the job still going',
        }
