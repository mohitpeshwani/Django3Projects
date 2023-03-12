from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length= 11)
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=150)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=100)
    
