from django.db import models

# Create your models here.
class in_out_rp(models.Model):
    rollno=models.CharField(max_length=15)
    name= models.CharField(max_length=40)
    intime = models.CharField(max_length=20)
    outtime = models.CharField(max_length=20)
    toggle = models.CharField(max_length=5)
    date = models.DateField()
class stud_rec(models.Model):
    rollno=models.CharField(max_length=15)
    name= models.CharField(max_length=40)
    