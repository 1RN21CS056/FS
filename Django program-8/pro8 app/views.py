from django.shortcuts import get_object_or_404, render, redirect
from .models import Course,Project,Student
from .forms import StudentForm, CourseForm,ProjectForm
from django.views.generic import ListView, DetailView

def index(request):
  courses = Course.objects.all()
  projects = Project.objects.all()
  students = Student.objects.all()
  return render(request, 'index.html', {'courses': courses,'projects': projects,'students':students})

def register_student(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = StudentForm()
  return render(request, 'register_student.html', {'form': form})

def register_course(request):
  if request.method == 'POST':
    form = CourseForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = CourseForm()
  return render(request, 'register_course.html', {'form': form})

def student_list(request, course_id):
  course = Course.objects.get(id=course_id)
  students = course.students.all()
  return render(request, 'student_list.html', {'students': students, 'course': course})

def student_detail(request, stu_id):
    student = get_object_or_404(Student, id=stu_id)
    return render(request, 'student_detail.html', {'student': student})

def project_details(request, project_id):
  project = get_object_or_404(Project, pk = project_id)
  return render(request, 'project_details.html', {'project': project})

def project_student_list(request, project_id):
  project = Project.objects.get(id=project_id)
  students = project.students.all()
  return render(request, 'project_student_list.html', {'students': students, 'project': project})

def register_project(request):
  if request.method == 'POST':
    form = ProjectForm(request.POST)
    if form.is_valid():
      project = form.save()
      return redirect('index')
      #return redirect('project_detail', project_id=project.pk)
  else:
    form = ProjectForm()
  return render(request, 'register_project.html', {'form': form})



class StudentListView(ListView):
  model = Student
  template_name = 'stu_list.html'
  context_object_name = 'students'

class StudentDetailView(DetailView):
  model = Student
  template_name = 'student_detail.html'
  context_object_name = 'student'

# Create your views here.
