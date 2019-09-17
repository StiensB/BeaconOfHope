from django.urls import path

from . import views

# Django convention is to have urls ending with a /

urlpatterns = [
    path("index/", views.index, name="index"),

    #home/login page
    path("", views.login, name="login"),
    #client stuff
    path("client/", views.client, name="client"),
    path("client/edit/<clientId>/", views.editClient, name="editClient"),
    path("client/edit/<clientId>/saveClient/", views.saveClient, name="saveClient"),
]