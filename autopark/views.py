from datetime import date
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Driver
from .forms import DriverForm, RegistrationFrom
# Create your views here.

def calculate_age(birthday):
    today = date.today()
    age = today.year - birthday.year
    if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
        age -= 1
    return age 

#=========DRIVER==========

def driver_registration(request):
    if request.method == "POST":
        reg_form = RegistrationFrom(request.POST)
        driver_form = DriverForm(request.POST)

        if reg_form.is_valid() and driver_form.is_valid():
            user = reg_form.save()
            driver = driver_form.seve(commit=False)
            driver.user = user
            driver.age = calculate_age(driver.birthday)
            driver.seve()
            # return redirect("driver_profile")
            return render(request, "autopark/driver_profile.html", {"form": driver})
        
    # Для метода GET   
    reg_form = RegistrationFrom()
    driver_form = DriverForm()
    context = {"reg_form": reg_form, "driver_form": driver_form}

    return render(request, "autopark/driver_form.html", context=context)

def driver_profile(request, pk):
    driver = Driver.objects.get(pk=pk)