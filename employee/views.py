from django.http import HttpResponse
from django.shortcuts import render,redirect
from employee.feedback import FeedbackForm
from employee.models import Employee,Testimonial,Feedback


# Create your views here.
def student_home(request):
    emps=Employee.objects.all()
    return render(request,"employee/employee_home.html",{'emps':emps})

def empdel(request,emp_id):
    x = Employee.objects.get(id=emp_id)
    print(id)
    x.delete()
    return redirect("/employee/home")

def empadd(request):
    if request.method=="POST":
        print("Data is comming properly")
        # fetching the data from the view form 
        name = request.POST.get('emp_name')
        department = request.POST.get('emp_department')
        emp_id = request.POST.get('emp_id')
        emp_no = request.POST.get('emp_phone_no')
        city = request.POST.get('emp_city')
        working = request.POST.get("working")

        #creating the employee object with given data
        new_entry = Employee()
        new_entry.employee_name = name
        new_entry.department = department
        new_entry.city = city
        new_entry.employee_id = emp_id
        new_entry.phone = emp_no
        if working == None:
            new_entry.working=False
        else:
            new_entry.working=True
        #save the object
        new_entry.save()
        #make the feedback message for new entry in the 
        return redirect("/employee/home")
    return render(request, "employee/employee_add.html",{})

def empupd(request,emp_id):
    x = Employee.objects.get(id = emp_id)
    return render(request , "employee/employee_update.html",{"x":x})


def do_update_emp(request,emp_id):
    if request.method=='POST':
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")  
    
        e=Employee.objects.get(pk=emp_id)
        e.employee_name=emp_name
        e.employee_id=emp_id_temp
        e.phone=emp_phone
        e.city=emp_address
        e.department=emp_department
        if e.working is None:
            e.working=False
        else:
            e.working=True

        e.save()
    return redirect("/employee/home/")

def testimonials(request):
    e=Testimonial.objects.all()

    return render(request, "employee/testimonials.html",{
        'e':e
    })


def feedback(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            v= form.save()
        else:
            return render(request, "employee/feedback.html",{'form':form})
    else:
        form=FeedbackForm()
        return render(request, "employee/feedback.html",{'form':form})
    return HttpResponse ("Saved successfully")
