from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Запись в блоге"""

    post_title = models.CharField(max_length=30, unique=True, )

    post_text = models.TextField(max_length=500)

    post_date = models.DateField(auto_now=True)

    post_image = models.ImageField(blank=True, upload_to='blog_app/post_images', default='')

    # def __str__(self):

    #  return 'id: '+str(self.id)+' text: '+self.post_title


class Comment(models.Model):
    """Комментарий к посту"""

    comment_post = models.ForeignKey(Post, related_name='comments')

    comment_text = models.TextField(max_length=500, )

    comment_date = models.DateField(auto_now_add=True)

    comment_author = models.ForeignKey(User, related_name='comments', default='')

    def __str__(self):
        return self.comment_text[:50]


class Subscribe(models.Model):
    """Подписка на новые сообщения"""

    subscribe_user = models.OneToOneField(User, default='')

    email = models.EmailField(unique=True)

    def __str__(self):
        # return User.objects.get(id=self.subscribe_user)

        return str(self.id) + "_" + self.email + "_" + str(self.subscribe_user.id)
