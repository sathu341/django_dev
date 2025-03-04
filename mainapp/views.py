from django.shortcuts import render
import pickle
import numpy as np


# Load the trained model
from django.shortcuts import render
from .forms import TipPredictionForm
from .utils import predict_tip
from .models import IndianRestaurantItem
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee,MenuEmployeeAssignment
from .forms import EmployeeForm
from django.core.mail import send_mail
import random
import string
from django.conf import settings
from django.contrib.auth.models import User
def empHome(request):
    emailid=request.session.get("empid")
    obj=Employee.objects.filter(email=emailid).first()
    if obj:
            request.session["empid"]=obj.id
            request.session["empname"]=obj.name
            return render(request,'employees/emphome.html',{'photo':obj.photo,"empname":obj.name})
    else:
        return redirect("emplogin/")

    
def empLogin(request):
    if request.method=="POST":
        emailid=request.POST.get("eml")
        password=request.POST.get("password")
        obj=Employee.objects.filter(email=emailid).first()
        if obj:
            request.session["empid"]=obj.id
            request.session["empname"]=obj.name
            return render(request,'employees/emphome.html',{'photo':obj.photo,"empname":obj.name})
        else:
            return render(request,'employees/empllogin.html',{'message':"invalid entery"})


    return render(request,'employees/empllogin.html',{"message":""})
def employee_duties(request):
    assignments = MenuEmployeeAssignment.objects.all()
    return render(request, 'employees/employee_duties.html', {'assignments': assignments})
# View Employee List
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

# Add New Employee
def generate_password(length=8):
    # Generate a random password with letters and digits
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save()

            # Generate a password for the new employee
            password = generate_password()

            # Create a new user for the employee (assuming email is the username)
            user = Employee.objects.filter(email=employee.email).last()
            user.password=password
            user.save()

            # Send email with login credentials
            subject = "Your Account Information"
            message = f"Hello {employee.name},\n\nYour account has been created successfully.\n\n" \
                      f"Your username is: {employee.email}\nYour password is: {password}\n\n" \
                      f"Please change your password after logging in."
            # from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [employee.email]
            # send_mail(subject, message, from_email, recipient_list)
            res=send_mail(subject,message,settings.EMAIL_HOST_USER,recipient_list)

            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'employees/add_employee.html', {'form': form})

# Edit Employee
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/edit_employee.html', {'form': form, 'employee': employee})

# Delete Employee
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

    return render(request, 'employees/delete_employee.html', {'employee': employee})

def index(request):
    items = IndianRestaurantItem.objects.all()
    return render(request,'index.html',{'items':items})

def item_list(request):
    items = IndianRestaurantItem.objects.all()
    return render(request, 'items/item_list.html', {'items': items})
def predict_tip_view(request):
    if request.method == 'POST':
        form = TipPredictionForm(request.POST)
        if form.is_valid():
            data = {
                'total_bill': [form.cleaned_data['total_bill']],
                'size': [form.cleaned_data['size']],
                f"sex_{form.cleaned_data['sex']}": [1],
                f"smoker_{form.cleaned_data['smoker']}": [1],
                f"day_{form.cleaned_data['day']}": [1],
                f"time_{form.cleaned_data['time']}": [1],
            }
            predicted_tip = predict_tip(data)
            return render(request, 'tip_predictor/predict_tip.html', {'form': form, 'predicted_tip': predicted_tip})
    else:
        form = TipPredictionForm()
    return render(request, 'tip_predictor/predict_tip.html', {'form': form})

