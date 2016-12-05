from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView
from .models import Post, Comment, Subscribe
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import Http404, HttpResponse
from .forms import CommentCreateForm, CreateSubscribeForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .tasks import comment_add_log, send_mail_to_subscribers

# Create your views here.


class PostsList(ListView):

    model = Post

    context_object_name = 'posts'

    def get_context_data(self, **kwargs):

        context = super(PostsList,self).get_context_data(**kwargs)

        if Subscribe.objects.filter(subscribe_user=self.request.user.id).exists():

            context['subscribe_id'] = (Subscribe.objects.get(subscribe_user=self.request.user.id)).id

        return context


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

#блок задач celery

            comment_add_log.delay(str(request.user))

            send_mail_to_subscribers.delay(form.cleaned_data['comment_text'])

#конец блока задач celery

            return redirect(reverse('comments_list', args=[pk]))

        raise Http404


class CommentDelete(DeleteView):

    model = Comment

    def get_success_url(self):

        comment = Comment.objects.get(id=self.kwargs.get('pk'))

        return reverse_lazy('comments_list', args=[comment.comment_post])

    def get(self,request,*args, **kwargs):

        return self.post(self,request,*args, *kwargs)


#TODO
class CreateSubscribe(CreateView ):

    template_name = 'blog_app/subscribe_create_form.html'

    form_class = CreateSubscribeForm

   #success_url = reverse_lazy('subscribe_create')

    def get_initial(self):

        return {'subscribe_user': self.request.user.id}

    def get_success_url(self):

        return reverse_lazy('post_list')

    #def get_context_data(self, **kwargs):

#        if not Subscribe.objects.filter(subscribe_user=self.request.user.id).exists():
#
 #           context = super(CreateView,self).get_context_data(**kwargs)
#
 #           return context

#        else:

 #           pass

    def get(self,request):

        if Subscribe.objects.filter(subscribe_user=self.request.user.id).exists():

            return HttpResponse('<p><h3>Вы уже подписаны</h3>')#redirect('post_list')

        else:

            return super(CreateView,self).get(request)


class DeleteSubscribe(DeleteView):

    model = Subscribe

    success_url = reverse_lazy('post_list')

    def get(self, request, *args, **kwargs):

        return self.post(self, request, *args, *kwargs)


