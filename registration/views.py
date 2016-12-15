from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserCreateForm


# Create your views here.


def registration_view(request):

    if request.POST:

        form = UserCreateForm(request.POST)

        if form.is_valid():

            form.save()

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

            if user:

                login(request, user)

            return redirect(reverse('post_list'))

        else:

            pass

    else:

        form = UserCreateForm()

    context = {'form': form}

    return render(request, 'registration/registration.html', context)



