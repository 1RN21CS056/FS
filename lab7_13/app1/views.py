from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from app1.forms import *
from app1.models import *
from django.views.generic import DetailView,ListView
import csv
from reportlab.pdfgen import canvas
def is_ajax(req):
    return req.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
def add_project(req):
    if req.method=='POST':
        form=ProjectForm(req.POST)
        if form.is_valid():
            form.save()
        return render(req, 'add_project.html',locals())
    form=ProjectForm()
    return render(req,'add_project.html',locals())
def add_student(req):
    if is_ajax(req):
        form=StudentForm(req.POST)
        if form.is_valid():
            form.save()
        return JsonResponse({'success':form.is_valid()})
    form=StudentForm()
    return render(req,'add_student.html',locals())
def search(req):
    if is_ajax(req):
        student=Student.objects.get(usn=req.GET.get('usn'))
        courses=",".join(str(j) for j in student.courses.all())
        data={'name':student.name,'usn':student.usn,'courses':courses}
        return JsonResponse(data)
    return render(req,"search.html")
def get_csv(req):
    res=HttpResponse(content_type="text/csv")
    res['Content-Disposition'] = 'attachment; filename="student.csv"'
    writer=csv.writer(res)
    writer.writerow(['name', 'usn', 'courses'])
    for i in Student.objects.all():
        courses=",".join(str(j) for j in i.courses.all())
        writer.writerow([i.name,i.usn,courses])
    return res
def get_pdf(req):
    res=HttpResponse(content_type="application/pdf")
    res['Content-Disposition'] = 'attachment; filename="student.pdf"'
    p = canvas.Canvas(res, pagesize=(600,800))
    y=750
    def entry(name,usn,course):
        d=p.drawString
        d(50,y,name)
        d(200,y,usn)
        d(300,y,course)
    entry('name','usn','courses')
    for i in Student.objects.all():
        courses=",".join(str(j) for j in i.courses.all())
        y-=15
        entry(i.name,i.usn,courses)
    p.showPage()
    p.save()
    return res

class StudentListView(ListView):
    model=Student
    template_name="students.html"
    context_object_name="students"
class StudentDetailView(DetailView):
    model=Student
    template_name="student.html"
    context_object_name="student"