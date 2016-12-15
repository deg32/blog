from rest_framework import generics

from .models import PostSerializer, CommentSerializer, Post, Comment


class PostListView(generics.ListAPIView):
    """ Список всех постов"""

    serializer_class = PostSerializer

    queryset = Post.objects.all()


class CommentListView(generics.ListAPIView):
    """Список комментариев к посту по номеру поста"""

    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(comment_post=self.kwargs['pk'])

        return queryset


class PostCreateView(generics.CreateAPIView):
    """Добавление поста"""

    serializer_class = PostSerializer


class CommentCreateView(generics.CreateAPIView):
    """Добавление комментария к посту"""
    serializer_class = CommentSerializer


class PostDeleteView(generics.DestroyAPIView):
    """Удаление поста"""

    serializer_class = PostSerializer

    queryset = Post.objects.all()


class CommentDeleteView(generics.DestroyAPIView):
    """Удаление комментария"""

    serializer_class = CommentSerializer

    queryset = Comment.objects.all()
