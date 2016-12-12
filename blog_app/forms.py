from django.forms import ModelForm
from .models import Comment, Post, Subscribe
from django.forms.widgets import HiddenInput
from django.forms import ValidationError


# форма создания комментария
class CommentCreateForm(ModelForm):

    class Meta:

        model = Comment

        fields = '__all__'

        widgets = {'comment_post': HiddenInput(), 'comment_author': HiddenInput()}

        labels = {'comment_text': 'Ваш комментарий'}


# форма создания подписки
class CreateSubscribeForm(ModelForm):

    class Meta:

        model = Subscribe

        fields = '__all__'

        widgets = {'subscribe_user': HiddenInput()}

        labels = {'email': 'Ваш адрес'}





