from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    age = models.IntegerField(max_length=3)
    is_Active = models.BooleanField(default=True)

