from django.forms import ModelForm
from django.forms.widgets import HiddenInput

from .models import Comment, Subscribe


class CommentCreateForm(ModelForm):
    """форма создания комментария к посту, используется в class CommentsList в файле blog_app/views.py"""

    class Meta:
        model = Comment

        fields = '__all__'

        widgets = {'comment_post': HiddenInput(), 'comment_author': HiddenInput()}

        labels = {'comment_text': ''}


class CreateSubscribeForm(ModelForm):
    """ форма создания подписки на новые комментарии"""

    class Meta:
        model = Subscribe

        fields = '__all__'

        widgets = {'subscribe_user': HiddenInput()}

        labels = {'email': 'Ваш адрес'}
