from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ("id", "firstName", "lastName", "dateOfBirth", "sex", "phoneNumber", "emailAddress", "lphResident",
                  "ownsCar", "hasLicense", "rideAvailable", "statusId", "dateCreated", "createdBy",
                  "lastUpdated", "updatedBy")