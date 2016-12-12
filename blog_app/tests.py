from django.test import TestCase
from .models import Post

# Create your tests here.

class TestModels(TestCase):

    def test_models_creation(self):

        post = Post(post_title ='555',post_text ='55555555555555555555555555555555555555555555555555')
        post.save()
        post = Post(post_title=str(), post_text =str())
        post.save()
        post = Post(post_title ='5556',post_text = '77777777777777777777777777777777777777777')
        post.save()