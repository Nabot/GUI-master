from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from read_data import print_data


# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")


def nata(request):
    return HttpResponse("<h1>This a simple page")

def temp(request):
    data = print_data()
    return HttpResponse("<h1>"+data+"</h1>")
