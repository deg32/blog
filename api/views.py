from django.shortcuts import render
from .models import PostSerializer, CommentSerializer, Post, Comment
from rest_framework import generics


#Список всех постов
class PostListView(generics.ListAPIView):

    serializer_class = PostSerializer

    queryset = Post.objects.all()


#Список комментариев к посту по номеру поста
class CommentListView(generics.ListAPIView):

    serializer_class = CommentSerializer

    def get_queryset(self):

        queryset = Comment.objects.filter(comment_post=self.kwargs['pk'])

        return queryset


#Добавление поста
class PostCreateView(generics.CreateAPIView):

    serializer_class = PostSerializer


#Добавление комментария к посту
class CommentCreateView(generics.CreateAPIView):

    serializer_class = CommentSerializer


#Удаление поста
class PostDeleteView(generics.DestroyAPIView):

    serializer_class = PostSerializer

    queryset = Post.objects.all()


#Удаление комментария
class CommentDeleteView(generics.DestroyAPIView):

    serializer_class = CommentSerializer

    queryset = Comment.objects.all()



