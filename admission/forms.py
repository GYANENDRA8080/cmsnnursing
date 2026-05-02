from django import forms
from .models import AdmissionEnquiry, HostelAdmission


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionEnquiry
        exclude = ['applied_on', 'status']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Father's Name"}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'programme': forms.Select(attrs={'class': 'form-select'}),
            'board_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Board / University Name'}),
            'passing_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Year of Passing'}),
            'percentage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Percentage (%)'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Permanent Address'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any additional message (optional)'}),
        }


class HostelForm(forms.ModelForm):
    class Meta:
        model = HostelAdmission
        exclude = ['applied_on']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'programme': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'guardian_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Guardian's Name"}),
            'guardian_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Guardian's Phone"}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Permanent Address'}),
        }
