from django.test import TestCase, Client
from django.urls import resolve

from .models import Post


# Create your tests here.

class TestModels(TestCase):
    client = Client()

    def test_post_creation(self):
        """Проверка создания новых постов"""

        post = Post(post_title='555', post_text='55555555555555555555555555555555555555555555555555')

        post.save()

        post = Post(post_text=str())

        post.save()

        post = Post(post_title='5556', post_text='77777777777777777777777777777777777777777')

        post.save()

        self.assertEqual(Post.objects.all().count(), 3)

    #def test_comment_creation(self):

    #    post = Post(id=1, post_title='555', post_text='55555555555555555555555555555555555555555555555555')

    #    post.save()

    #    post = Post.objects.get(id=1)

    #    comment = Comment (comment_post=, comment_text=,comment_date=)

    def test_url_resolve(self):
        """Проверка разрешения URL-ей"""

        r = resolve('/blog/posts/')

        self.assertEqual(r.func.__name__, 'PostsList')

        r = resolve('/blog/subscribe/add')

        self.assertEqual(r.func.__name__, 'CreateSubscribe')

        r = resolve('/blog/detail/1/')

        self.assertEqual(r.func.__name__, 'PostDetail')

    def test_client_without_login(self):
        """Перенаправление при попытке просмотра деталей поста"""

        code = self.client.get('/blog/detail/2').status_code

        self.assertEqual(code, 301)

    def test_client_login(self):

        self.client.post('/registration/login/', {'name': 'deg32', 'password': '1qazxsw2'})

    #     code = self.client.get('/blog/detail/12/',).status_code


