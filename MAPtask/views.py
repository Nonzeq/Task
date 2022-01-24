from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView
from .forms import *
from .utils import *


def index(request):
    return render(request, 'MAPtask/index.html')


class AddUser(CreateView):
    """Представлення форми для привітання"""
    form_class = AddUserForm
    template_name = 'MAPtask/index.html'
    login_url = '/admin/'

    def get_success_url(self):
        if self.request.method == 'POST':
            data = self.request.POST.get('fist_name', '')
        try:
            User.objects.get(fist_name=data)
            return reverse('user', kwargs={'user_id': self.object.pk, 'fist_name': self.object.fist_name})
        except:
            return reverse('hi_user', kwargs={'user_id': self.object.pk, 'fist_name': self.object.fist_name})


class ShowUser(DataMixin, DetailView):
    """Представлення для першого юзера"""
    model = User
    template_name = 'MAPtask/ShowUser.html'
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'


class HiUser(DetailView):
    """Представлення для юзера який є в базі"""
    model = User
    template_name = 'MAPtask/hi_user.html'
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'


class ListUsers(ListView):
    """Представлення усіх хто привітався"""
    paginate_by = 6
    model = User
    template_name = 'MAPtask/user_list.html'
    context_object_name = 'user'

    def get_queryset(self):
        users = User.objects.all()
        users.distinct()
        return users











