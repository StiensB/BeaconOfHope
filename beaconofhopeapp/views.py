from django.shortcuts import redirect, render
from django.db.models import Q# Complex Lookups

from .models import Client, Company#, Login
from .forms import ClientForm, CompanyForm#, LoginForm

# Create your views here.
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm, UserProfileForm
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import RequestContext

def register(request):
        context = RequestContext(request)
        registered = False
        if request.method == 'POST':
                uform = UserForm(data = request.POST)
                pform = UserProfileForm(data = request.POST)
                if uform.is_valid() and pform.is_valid():
                        user = uform.save()
                        # form brings back a plain text string, not an encrypted password
                        pw = user.password
                        # thus we need to use set password to encrypt the password string
                        user.set_password(pw)
                        user.save()
                        profile = pform.save(commit = False)
                        profile.user = user
                        profile.save()
                        registered = True
                else:
                        print (uform.errors, pform.errors)
        else:
                uform = UserForm()
                pform = UserProfileForm()

        return render(request, 'register/register.html', {'uform': uform, 'pform': pform, 'registered': registered })

def user_login(request):
    print(0)
    context = RequestContext(request)
    print(-1)
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          print (1)
          if user is not None:
              if user.is_active:
                  print (2)
                  # Redirect to index page.
                  return redirect("/index/")
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print  ("invalid login details " + username + " " + password)
              return redirect("/login/")
    else:
        print(34535)
        # the login is a  GET request, so just show the user the login form.
        return render(request, 'login/login.html')

@login_required
def user_logout(request):
    context = RequestContext(request)
    logout(request)
    # Redirect back to index page.
    return HttpResponseRedirect('/login')

# template page
def index(request):
    return render(request, "beaconofhope/index.html")

# # login/home page
# def login(request):
#     form = LoginForm()
#     return render(request, "login/login.html", {"form": form})

# client page
@login_required
def client(request):
    allClients = Client.objects.all()
    query = request.GET.get("query")
    if query:
        allClients = allClients.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(email_address__icontains=query)) 

            
    return render(request, "client/client.html", { "allClients": allClients})

# edit client page
@login_required
def editClient(request, clientId):
    client = Client.objects.get(id = clientId)
    form = ClientForm(instance =client)
    return render(request, "client/edit.html", { "form": form, "clientId": clientId })

# save client page
@login_required
def saveClient(request, clientId):
    client = Client.objects.get(id = clientId)
    form = ClientForm(request.POST, instance=client)
    form.save()
    return redirect("/client")

# add client page
@login_required
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
@login_required
def company(request):
    allCompanies = Company.objects.all()
    return render(request, "company/company.html", { "allCompanies": allCompanies})

# edit company page
@login_required
def editCompany(request, companyId):
    company = Company.objects.get(id = companyId)
    form = CompanyForm(instance =company)
    return render(request, "company/edit.html", { "form": form, "companyId": companyId })

#view company page
@login_required
def viewCompany(request, companyId):
    companyId = Company.objects.get(id = companyId)
    return render(request, "company/view.html", { "companyId": companyId })

# save company page
@login_required
def saveCompany(request, companyId):
    company = Company.objects.get(id = companyId)
    form = CompanyForm(request.POST, instance=company)
    form.save()
    return redirect("/company")

# add company page
@login_required
def addCompany(request):
    if(request.method == "POST"):
        form = CompanyForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/company")
    else:
        form = CompanyForm()
    return render(request, "company/addCompany.html", {"form":form})
