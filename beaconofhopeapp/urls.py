from django.urls import path

from . import views

# Django convention is to have urls ending with a /

urlpatterns = [
    path("index/", views.index, name="index"),

    #home/login page
    path("", views.login, name="login"),

]