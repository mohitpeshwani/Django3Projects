from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length= 11)
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=150)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.employee_name + " "+ self.employee_id
    
class Testimonial(models.Model):
    name = models.CharField(max_length=50,null=True)
    testimonial = models.TextField(null=True)
    image = models.ImageField(upload_to="testimonial/", height_field=None, width_field=None, max_length=None,null=True)
    rating = models.IntegerField(null=True)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email =models.CharField(max_length=100)
    feedback = models.TextField()