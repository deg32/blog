from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):

    post_title = models.CharField(max_length=30,unique=True)

    post_text = models.TextField(max_length=500)

    post_date = models.DateField(auto_now=True)

    post_image = models.ImageField(blank=True, upload_to='blog_app/post_images', default='')

    def __str__(self):

        return self.post_title


class Comment(models.Model):

    comment_post = models.ForeignKey(Post, related_name='comments')

    comment_text = models.TextField(max_length=500, )

    comment_date = models.DateField(auto_now_add=True)

    comment_author = models.ForeignKey(User, related_name='comments', default='')


class Subscribe(models.Model):

    subscribe_user = models.ForeignKey(User, default='')

    email = models.EmailField(unique=True)

    def __str__(self):

        #return User.objects.get(id=self.subscribe_user)

        return self.email




