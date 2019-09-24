from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Client
from .models import Company

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ("id", "firstName", "lastName", "dateOfBirth", "sex", "phoneNumber", "emailAddress", "lphResident",
                  "ownsCar", "hasLicense", "rideAvailable", "statusId", "dateCreated", "createdBy",
                  "lastUpdated", "updatedBy")

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ("id", "name", "primaryFirstName", "primaryLastName", "primaryPhone", "primaryEmail", "address1",
                  "address2", "city", "state", "zipCode", "neighborHoodId", "dateCreated", "createdBy", "lastUpdated",
                  "updatedBy", "dateReviewed", "reviewedBy")
