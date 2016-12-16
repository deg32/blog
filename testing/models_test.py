# coding=utf-8
from blog_app.models import Post


def test_post_creation():
    """Проверка на создание новых постов"""

    post = Post(post_title='555', post_text='55555555555555555555555555555555555555555555555555')

    post.save()

    post = Post(post_text=str())

    post.save()

    post = Post(post_title='5556', post_text='77777777777777777777777777777777777777777')

    post.save()

    assert(Post.objects.all().count()) == 3