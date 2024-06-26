from django.db import models

# Create your models here.
class Project(models.Model):
    studentname=models.CharField(max_length=200)
    ptopic=models.CharField(max_length=200)
    planguages=models.CharField(max_length=200)
    pduration=models.IntegerField()