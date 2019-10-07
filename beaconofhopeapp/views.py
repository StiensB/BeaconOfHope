from django.shortcuts import redirect, render

from .models import Client, Company, Login
from .forms import ClientForm, CompanyForm, LoginForm

# Create your views here.

# template page
def index(request):
    return render(request, "beaconofhope/index.html")

# login/home page
def login(request):
    form = LoginForm()
    return render(request, "login/login.html", {"form": form})

# client page
def client(request):
    allClients = Client.objects.all()
    return render(request, "client/client.html", { "allClients": allClients})

# edit client page
def editClient(request, clientId):
    client = Client.objects.get(id = clientId)
    form = ClientForm(instance =client)
    return render(request, "client/edit.html", { "form": form, "clientId": clientId })

# save client page
def saveClient(request, clientId):
    client = Client.objects.get(id = clientId)
    form = ClientForm(request.POST, instance=client)
    form.save()
    return redirect("/client")

# add client page
def addClient(request):
    if(request.method == "POST"):
        form = ClientForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/client")
    else:
        form = ClientForm()
    return render(request, "client/addClient.html", {"form":form})


# company page
def company(request):
    allCompanies = Company.objects.all()
    return render(request, "company/company.html", { "allCompanies": allCompanies})

# edit company page
def editCompany(request, companyId):
    company = Company.objects.get(id = companyId)
    form = CompanyForm(instance =company)
    return render(request, "company/edit.html", { "form": form, "companyId": companyId })

# save company page
def saveCompany(request, companyId):
    company = Company.objects.get(id = companyId)
    form = CompanyForm(request.POST, instance=company)
    form.save()
    return redirect("/company")

# add company page
def addCompany(request):
    if(request.method == "POST"):
        form = CompanyForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/company")
    else:
        form = CompanyForm()
    return render(request, "company/addCompany.html", {"form":form})
