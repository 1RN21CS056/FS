from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import ProjectReg

# Create your views here.
def add_project(request):
    if request.method == "POST":
        form=ProjectReg(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Record Inserted Successfully</h1>")
        else:
            return HttpResponse("<h1> Record Not Inserted</h1>")
        
    else:
        form=ProjectReg()
        return render(request, "add_project.html",{"form":form})    
