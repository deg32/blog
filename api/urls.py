from django.conf.urls import url

from .views import PostListView, CommentListView, PostCreateView, CommentCreateView, PostDeleteView, CommentDeleteView

urlpatterns = [

    # все посты
    url(r'posts/', PostListView.as_view(), name='rest_posts_list'),

    # комментарии к посту
    url(r'comments/(?P<pk>\d+)/', CommentListView.as_view(), name='rest_comments_list'),

    # добавление нового поста
    url(r'post/add/', PostCreateView.as_view(), name='rest_post_add'),

    # добавление нового комментария
    url(r'comment/add/', CommentCreateView.as_view(), name='rest_comment_add'),

    # удаление поста по номеру
    url(r'post/delete/(?P<pk>\d+)/', PostDeleteView.as_view(), name='rest_post_delete'),

    # удаление комментария по номеру
    url(r'comment/delete/(?P<pk>\d+)/', CommentDeleteView.as_view(), name='rest_comment_delete'),

]
