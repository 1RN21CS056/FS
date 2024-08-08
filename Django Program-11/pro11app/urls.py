from django.urls import path
from .views import student,search_students

urlpatterns = [
  path('student/',student,name='student'),
  path('search/',search_students,name = 'search_students'),
]