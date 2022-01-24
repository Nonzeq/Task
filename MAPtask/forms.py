from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import *


class AddUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['fist_name']
        widgets = {
            'fist_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def fist_name(self):
        fist_name = self.cleaned_data['fist_name']
        return fist_name



