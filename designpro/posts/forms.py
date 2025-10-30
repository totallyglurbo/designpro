from django import forms
from django.contrib.auth.forms import UserCreationForm
import re

class RegistrationForm(UserCreationForm):
    login = forms.CharField(max_length=150, required=True, unique=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    patronymic = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, required=True)
    password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirm', required=True, widget=forms.PasswordInput)
    agreement = forms.BooleanField(required=True)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not re.match(r'^[А-яёЁ -]+$', first_name):
            raise forms.ValidationError('Please enter a valid name.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not re.match(r'^[А-яёЁ -]+$', last_name):
            raise forms.ValidationError('Please enter a valid name.')
        return last_name

    def clean_patronymic_name(self):
        patronymic_name = self.cleaned_data['first_name']
        if not re.match(r'^[А-яёЁ -]+$', patronymic_name):
            raise forms.ValidationError('Please enter a valid name.')
        return patronymic_name

    def clean_login(self):
        login = self.cleaned_data['login']
        if not re.match(r'^[A-z -]', login):
            raise forms.ValidationError('Please enter a valid login.')
        return login

    def clean_email(self):
        email = self.cleaned_data['email']
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return cleaned_data




