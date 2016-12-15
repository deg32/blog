from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    error_messages = {'password_mismatch': 'Ой, пароли не совпадают'}

    help_texts = {'password2': '1'}

    labels = {'username': 'Пользователь'}
