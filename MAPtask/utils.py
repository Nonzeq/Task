from .forms import *
from .models import *


user = [
    {'title': 'Привіт', 'ulr_name': 'user'},
    {'title': 'Бачились', 'ulr_name': 'user'},
]


class DataMixin:
    paginate_by = 6
    def get_user_context(self, **kwargs):
        context = kwargs
        users = User.objects.all()
        #если юзер не авторизован - добавить статью
        context['user'] = users
        return context