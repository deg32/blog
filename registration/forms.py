from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreateForm(UserCreationForm):

    error_messages = {'password_mismatch': 'Ой, пароли не совпадают'}

    help_texts = {'password2': '1'}

    labels = {'username' : 'Пользователь'}