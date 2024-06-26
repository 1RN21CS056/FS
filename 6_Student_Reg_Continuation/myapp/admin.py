from django.contrib import admin
from myapp.models import Course, Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('student_name', 'student_usn', 'student_sem')
    ordering=('student_name',)
    search_fields=('student_name',)
admin.site.register(Course)    
