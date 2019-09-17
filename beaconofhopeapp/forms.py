from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ("firstName", "lastName", "dateOfBirth", "sex", "phoneNumber", "emailAddress")