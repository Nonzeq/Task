from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', AddUser.as_view(), name='home'),
    path('hi_user/<int:user_id>/<str:fist_name>', HiUser.as_view(), name='hi_user'),
    path('ShowUser/<int:user_id>/<str:fist_name>', ShowUser.as_view(), name='user'),
    path('list_users/', ListUsers.as_view(), name='list_users'),

]