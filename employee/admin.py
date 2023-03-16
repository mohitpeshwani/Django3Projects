from django.contrib import admin
from employee.models import Employee
from employee.models import Testimonial
from employee.models import Feedback
class EmpAdmin(admin.ModelAdmin):
    list_display=['employee_name','working']
    list_filter = ['working','employee_name'] 
    search_field =["employee_name","id","employee_id","working"]


admin.site.register(Employee,EmpAdmin) 
admin.site.register(Testimonial)
admin.site.register(Feedback)

