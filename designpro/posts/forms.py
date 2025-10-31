from django import forms
import re
from .models import ReallyUser


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label="Имя пользователя")
    first_name = forms.CharField(max_length=50, required=True, label="Имя")
    last_name = forms.CharField(max_length=50, required=True, label="Фамилия")
    patronymic = forms.CharField(max_length=50, required=True, label="Отчество")
    email = forms.EmailField(max_length=254, required=True, label="Электронная почта")
    password1 = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', required=True, widget=forms.PasswordInput)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not re.match(r'^[А-яёЁ -]+$', first_name):
            raise forms.ValidationError('Имя должно содержать только кириллицу.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not re.match(r'^[А-яёЁ -]+$', last_name):
            raise forms.ValidationError('Фамилия должна содержать только кириллицу.')
        return last_name

    def clean_patronymic_name(self):
        patronymic_name = self.cleaned_data['first_name']
        if not re.match(r'^[А-яёЁ -]+$', patronymic_name):
            raise forms.ValidationError('Отчество должно содержать только кириллицу')
        return patronymic_name

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^[A-z -]', username):
            raise forms.ValidationError('Имя пользователя должно содержать только латиницу.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпадают.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = ReallyUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'patronymic', 'email', 'agreement')

#




