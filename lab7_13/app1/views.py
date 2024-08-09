from django.shortcuts import render
from django.http import JsonResponse
from app1.forms import *
from app1.models import *
from django.views.generic import DetailView,ListView
def is_ajax(req):
    return req.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
def add_project(req):
    if req.method=='POST':
        form=ProjectForm(req.POST)
        if form.is_valid():
            form.save()
        return render(req, 'add_project.html',locals())
    else:
        form=ProjectForm()
        return render(req,'add_project.html',locals())
def add_student(req):
    print("call")
    if req.method=='POST':
        form=StudentForm(req.POST)
        if form.is_valid():
            form.save()
        print("ye")
        if is_ajax(req):
            return JsonResponse({'success':True})
        else:
            return render(req, 'add_student.html',locals()) 
    else:
        form=StudentForm()
        return render(req,'add_student.html',locals())
def search(req):
    if is_ajax(req):
        # print("read as ajax",req.GET.get('usn'))
        student=Student.objects.get(usn=req.GET.get('usn'))
        # print(student.courses.all())
        courses=""
        for i in student.courses.all():
            courses+=i.name+","
        data={'name':student.name,'usn':student.usn,'courses':courses}
        # print(data)
        return JsonResponse(data)
    else:
        return render(req,"search.html")
    
    
class StudentListView(ListView):
    model=Student
    template_name="students.html"
    context_object_name="students"
class StudentDetailView(DetailView):
    model=Student
    template_name="student.html"
    context_object_name="student"