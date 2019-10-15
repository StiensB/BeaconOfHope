from django.urls import path

from . import views

# Django convention is to have urls ending with a /

urlpatterns = [
    path("", views.index, name="index"),

    #home/login page
    path("login/", views.user_login, name="login"),
    #logout page
    path("logout/", views.user_logout, name="logout"),
    #register page
    path("register/", views.register, name='register'),
    #client stuff
    path("client/", views.client, name="client"),
    path("client/edit/<clientId>/", views.editClient, name="editClient"),
    path("client/edit/<clientId>/saveClient/", views.saveClient, name="saveClient"),
    path("client/addClient/", views.addClient, name="addClient"),
    #company stuff
    path("company/", views.company, name="company"),
    path("company/view/<companyId>/", views.viewCompany, name="viewCompany"),
    path("company/edit/<companyId>/", views.editCompany, name="editCompany"),
    path("company/edit/<companyId>/saveCompany/", views.saveCompany, name="saveCompany"),
    path("company/addCompany/", views.addCompany, name="addCompany")

]
