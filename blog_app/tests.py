from django.test import TestCase

from .models import Post


# Create your tests here.

class TestModels(TestCase):
    def test_post_creation(self):
        post = Post(post_title='555', post_text='55555555555555555555555555555555555555555555555555')

        post.save()

        post = Post(post_text=str())

        post.save()

        post = Post(post_title='5556', post_text='77777777777777777777777777777777777777777')

        post.save()

        self.assertEqual(Post.objects.all().count(), 3)

    def test_comment_creation(self):
        post = Post(id=1, post_title='555', post_text='55555555555555555555555555555555555555555555555555')

        post.save()

        post = Post.objects.get(id=1)

        # comment = Comment (comment_post=, comment_text=,comment_date=)
