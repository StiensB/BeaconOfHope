from django.shortcuts import redirect, render

from .forms import ClientForm
from .models import Client

# Create your views here.

# template page
def index(request):
    return render(request, "beaconofhope/index.html")

# login/home page
def login(request):
    return render(request, "login/login.html")

def client(request):
    allClients = Client.objects.all()
    return render(request, "client/client.html", { "allClients": allClients})

def editClient(request, clientId):
    client = Client.objects.get(id = clientId)
    form = ClientForm(instance =client)
    return render(request, "client/edit.html", { "form": form, "clientId": clientId })

def saveClient(request, clientId):
    client = Client.objects.get(id = clientId)
    form = ClientForm(request.POST, instance=client)
    form.save()
    return redirect("/client")

def addClient(request):
    if(request.method == "POST"):
        form = ClientForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/client")
    else:
        form = ClientForm()
    return render(request, "client/addClient.html", {"form":form})

