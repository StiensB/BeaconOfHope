from django.shortcuts import render

# Create your views here.

# template page
def index(request):
    return render(request, "beaconofhope/index.html")

# login/home page
def login(request):
    return render(request, "login/login.html")