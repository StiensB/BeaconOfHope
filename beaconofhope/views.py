from django.shortcuts import render

# Create your views here.

# home
def index(request):
    return render(request, "beaconofhope/index.html")