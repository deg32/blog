from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView
from .models import Post, Comment, Subscribe
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import Http404
from .forms import CommentCreateForm, CreateSubscribeForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError

# Create your views here.


class PostsList(ListView):

    model = Post

    context_object_name = 'posts'


class PostDetail(LoginRequiredMixin,DetailView):

    login_url = reverse_lazy('login')

    model = Post

    context_object_name = 'post'

    def get_object(self, queryset=None):

        return get_object_or_404(Post, id=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):

        comments = Comment.objects.all().order_by('comment_date')[0:5]

        context = super(PostDetail,self).get_context_data (**kwargs)

        context['comments'] = comments

        return context


class CommentsList(ListView):

    model = Comment

    context_object_name = 'comments'

    def get_queryset(self):

        if Post.objects.filter(id=self.kwargs.get('pk')).exists():

            return Comment.objects.filter(comment_post_id=self.kwargs.get('pk'))

        else:

            raise Http404

    def get_context_data(self, **kwargs):

        pk = self.kwargs.get('pk')

        context = super(CommentsList,self).get_context_data(**kwargs)

        context['form'] = CommentCreateForm(initial={'comment_post': pk, 'comment_author': self.request.user})

        return context


class CommentCreate(View):

   def post(self, request):

        form = CommentCreateForm(request.POST)

        if form.is_valid():

            pk = form.cleaned_data.get('comment_post')

            form.save()

            return redirect(reverse('comments_list', args=[pk]))

        raise Http404


class CommentDelete(DeleteView):

    model = Comment

    def get_success_url(self):

        comment = Comment.objects.get(id=self.kwargs.get('pk'))

        return reverse_lazy('comments_list', args=[comment.comment_post])

    def get(self,request,*args, **kwargs):

        return self.post(self,request,*args, *kwargs)


class CreateSubscribe(CreateView):

    template_name = 'blog_app/subscribe_create_form.html'

    def post(self, request, *args, **kwargs):

        form = CreateSubscribeForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(reverse('post_list'))

        else:

            return redirect(request.path)

    def get_context_data(self, **kwargs):

        context = super(CreateView,self).get_context_data(**kwargs)

        context['form']= CreateSubscribeForm(initial={'subscribe_user': self.request.user.id})

        return context






