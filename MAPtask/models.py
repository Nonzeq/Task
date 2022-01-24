from django.db import models
from django.urls import reverse, reverse_lazy


# Create your models here.



class User(models.Model):

    fist_name = models.CharField(max_length=128, verbose_name="Ім'я")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Публікація')

    def __str__(self):
        return self.fist_name


    def get_absolute_url(self):
        return reverse('user', kwargs={'user_id': self.pk, 'fist_name': self.fist_name })

