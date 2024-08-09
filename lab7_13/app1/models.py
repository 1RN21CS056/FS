from django.db import models

# Create your models here
class Course(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Student(models.Model):
    name=models.CharField(max_length=100)
    usn=models.CharField(max_length=20,unique=True)
    courses=models.ManyToManyField(Course, blank=True, related_name='Student')
    def __str__(self):
        return self.name+"/"+self.usn
class Language(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Project(models.Model):
    topic=models.CharField(max_length=100)
    languages=models.ManyToManyField(Language)
    duration=models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    def __str__(self):
        return self.topic
