from django import forms
from .models import StudentModel


class StudentForm(forms.ModelForm):
    name = forms.CharField(label='Name',max_length=100,widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Name...'
    }), required=True)

    age = forms.CharField(label='Age', max_length=20, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Age...'
    }), required=True)

    address = forms.CharField(label='Address', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Address...'
    }), required=True)

    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Email...'
    }), required=True)

    pin = forms.CharField(label='Pin', max_length=6, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Name...'
    }), required=True)

    mob = forms.CharField(label='Mobile No.', max_length=11, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Name...'
    }), required=True)

    class Meta():
        model=StudentModel
        fields=['name', 'age', 'address', 'email', 'pin', 'mob']