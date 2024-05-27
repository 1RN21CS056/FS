from datetime import date
from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def aboutus(request):
    return render(request, "aboutus.html")

def contactus(request):
    return render(request, "contactus.html")


    
