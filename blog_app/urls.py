from django.conf.urls import url

from .views import PostsList, PostDetail, CommentsList, CommentCreate, CommentDelete, CreateSubscribe, DeleteSubscribe

urlpatterns = [

    url(r'posts/', PostsList.as_view(), name='post_list'),

    url(r'detail/(?P<pk>\d+)/', PostDetail.as_view(), name='post_detail'),

    url(r'comments/(?P<pk>\d+)/', CommentsList.as_view(), name='comments_list'),

    url(r'comment/add/', CommentCreate.as_view(), name='comment_create'),

    url(r'subscribe/add', CreateSubscribe.as_view(), name='subscribe_create'),

    url(r'subscribe/delete/(?P<pk>\d+)/', DeleteSubscribe.as_view(), name='subscribe_delete'),

    url(r'comment/delete/(?P<pk>\d+)/', CommentDelete.as_view(), name='comment_delete'),

    # url(r'registration/login/', auth_views.login, name='login'),
]
