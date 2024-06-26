from django.shortcuts import render
from django.http import HttpResponse 
from myapp.models import Course, Student 

# Create your views here.
def reg(request): 
    if request.method == "POST": 
        sid=request.POST.get("sname") 
        cid=request.POST.get("cname") 
        student1=Student.objects.get(id=sid) 
        course1=Course.objects.get(id=cid) 
        res=student1.enrolment.filter(id=cid) 
        if res: 
           return HttpResponse("<h1>Student already enrolled</h1>") 
        student1.enrolment.add(course1) 
        return HttpResponse("<h1>Student enrolled successfully</h1>") 
    else: 
        students=Student.objects.all() 
        courses=Course.objects.all() 
        return render(request,"reg.html",{"students":students, "courses":courses}) 
    
def course_search(request): 
    if request.method=="POST": 
        cid=request.POST.get("cname") 
        s=Student.objects.all() 
        student_list=list() 
        for student1 in s: 
            if student1.enrolment.filter(id=cid): 
                student_list.append(student1) 
        if len(student_list)==0: 
            return HttpResponse("<h1>No Students enrolled</h1>") 
        return render(request,"selected_students.html",{"student_list":student_list}) 
    else: 
        courses=Course.objects.all() 
        return render(request,"course_search.html",{"courses":courses})