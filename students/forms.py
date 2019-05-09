from django import forms
from .models import *
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(),required=True, max_length=100)
    email_id = forms.EmailField(widget=forms.EmailInput(),required=True)
    contact_no = forms.CharField(widget=forms.NumberInput(), required=True, max_length=11)

    class Meta:
        model = Student1
        fields = ['name', 'email_id', 'contact_no']


class UserForm(forms.ModelForm):
        username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username...'}), required=True, max_length=50)
        email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Id...'}), required=True, max_length=50)
        first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter First Name...'}), required=True, max_length=50)
        last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lasr Name...'}), required=True, max_length=50)
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password...'}), required=True, max_length=50)
        confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Cinfirm Password...'}), required=True, max_length=50)

        class Meta():
            model = User
            fields = ['username', 'email', 'first_name', 'last_name', 'password']