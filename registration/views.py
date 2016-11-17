from django.shortcuts import render, redirect
from .forms import UserCreateForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def registration_view(request):

    if request.POST:

        form = UserCreateForm(request.POST)

        if form.is_valid():

            form.save()

            #messages.success(request,'Пользователь создан')

            return redirect (reverse('post_list'))


        else:

            context = {'form': form}

            messages.error(request, 'Ошибка')

    else:

        form = UserCreateForm()

    context = {'form': form}

    return render(request, 'registration/registration.html', context)


def subscription(request):

    pass
