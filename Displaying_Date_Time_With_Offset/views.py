from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
# def home(request):
#     return HttpResponse("Hello world!")


#creating our views here

def current_time(request):
    return HttpResponse("The time is "+str(datetime.datetime.now()))

def hours_offset_increase(request, offset):
    return HttpResponse("After "+str(offset)+"hours the time will be "+str(datetime.datetime.now()+datetime.timedelta(hours = offset)))

def hours_offset_decrease(request, offset):
    return HttpResponse("Before "+str(offset)+"hours the time was"+str(datetime.datetime.now()-datetime.timedelta(hours = offset)))
