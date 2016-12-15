from rest_framework import serializers

from blog_app.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    """Cериализатор постов"""

    class Meta:

        model = Post

        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор комментариев"""

    class Meta:

        model = Comment

        fields = '__all__'

