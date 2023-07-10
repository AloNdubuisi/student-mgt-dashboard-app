from django.db import models

# Create your models here.
class Student(models.Model):
    regnum = models.CharField(max_length=100)
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='media')