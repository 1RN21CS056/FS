from django.shortcuts import render
from django.template import Template, context
from django.http import HttpResponse

# Create your views here.
def fruit_student(request):
    fruitList=["Apple", "Mango", "Orange"]
    StudentList=["Dilip", "Harsh", "Avinash"]
    return render(request, "Fruit_Student_List.html", {"fruitList":fruitList,"StudentList":StudentList})
    



