from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Client, Company#, Login
from .models import UserProfile
from django.contrib.auth.models import User

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ("id", "first_name", "last_name", "date_of_birth", "sex", "phone_number", "email_address", "lph_resident",
                  "owns_car", "has_license", "ride_available", "status", "date_created", "created_by",
                  "last_updated", "updated_by")

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ("id", "name", "primary_first_name", "primary_last_name", "primary_phone", "primary_email", "address1",
                  "address2", "city", "state", "zip_code", "neighborhood", "date_created", "created_by", "last_updated",
                  "updated_by", "date_reviewed", "reviewed_by")

class UserForm(ModelForm):
        class Meta:
                model = User
                fields = ["username", "email", "password"]

class UserProfileForm(ModelForm):
        class Meta:
                model = UserProfile
                fields = ['group']
