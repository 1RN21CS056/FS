from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Student
from .forms import StudentForm

def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})


def search_students(request):
  is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
  if is_ajax:
    query = request.GET.get('query', '')
    students = Student.objects.filter(first_name__icontains=query) | Student.objects.filter(last_name__icontains=query)
    results = []
    for student in students:
      student_data = {
        'id': student.id,
        'name': f"{student.first_name} {student.last_name}",
        'email': student.email,
        'courses': [course.name for course in student.courses.all()]
        }
      results.append(student_data)
    return JsonResponse({'results': results})
  return render(request, 'search.html')