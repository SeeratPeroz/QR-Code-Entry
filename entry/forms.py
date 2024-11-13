from django import forms
from .models import Patient, Entry

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'dob']

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['patient']
