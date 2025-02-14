from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)