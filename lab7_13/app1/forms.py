from django import forms
from app1.models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("topic","student","languages","duration")
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name","usn")
