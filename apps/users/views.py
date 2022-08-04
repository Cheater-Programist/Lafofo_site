import django
from django.db import models
from django.shortcuts import render
from apps import users
from apps.users.models import User
from apps.users.forms import UserCreateForm,UserCreationForm,UserRegistrateForm
from django.views import generic
from django.urls import reverse_lazy

class UserCreateView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'account/login.html'


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/update.html'

class UserDetailView(generic.DeleteView):
    model = User
    template_name = 'users/detail.html'
    contex_object_name = 'user'

class UserdeleteView(generic.DeleteView):
    model = User
    success_url = reverse_lazy('login')
    template_name = 'users/delete.html'