from django import forms
from .models import *
from django.contrib.auth.models import User, Group


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


class UserForm(forms.ModelForm):
        username = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username...'}), required=True,
            max_length=50)
        email = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Id...'}), required=True,
            max_length=50)
        first_name = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name...'}),
            required=True, max_length=50)
        last_name = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lasr Name...'}), required=True,
            max_length=50)
        password = forms.CharField(
            widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password...'}),
            required=True, max_length=50)
        confirm_password = forms.CharField(
            widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Cinfirm Password...'}),
            required=True, max_length=50)
        role = forms.ModelChoiceField(queryset=Group.objects.all())

        class Meta():
            model = User
            fields = ['username', 'email', 'first_name', 'last_name', 'password']
            label = {'password': 'password'}

        def __init__(self, *args, **kwargs):
            if kwargs.get('instance'):
                initial = kwargs.setdefault('initial', {})
                if kwargs['instance'].groups.all():
                    initial['role'] = kwargs['instance'].groups.all()[0]
                else:
                    initial['role'] = None

            forms.ModelForm.__init__(self, *args, **kwargs)

        def save(self):
            password = self.cleaned_data.pop('password')
            role = self.cleaned_data.pop('role')
            u = super().save()
            u.groups.set([role])
            u.set_password(password)
            u.save()
            return u