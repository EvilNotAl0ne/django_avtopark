from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Driver


class RegistrationFrom(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email"]
        
        labels = {
        'username': 'Логин',
        'email': 'Эл. почта',
        'password1': 'Пароль',
        'password2': 'Повторить пароль',
        }
        help_text = {
        'username': '',
        'password1': '',
        }

class DriverForm(forms.ModelForm):
    birthday = forms.DateField(label='Дата рождения', widget=forms.DateInput(format='%d.%m.%Y'), input_formats=['%d.%m.%Y'])
    class Meta:
        model = Driver
        exclude = ["user", "is_available"]