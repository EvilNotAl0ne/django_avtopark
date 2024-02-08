from django.shortcuts import render
from django.views.generic import CreateView

from .models import Driver
from .forms import DriverModelFrom

# Create your views here.

#=========driver==========
class DriverCreate(CreateView):
    model = Driver
    form_class = DriverModelFrom
    template_name = "autopark/driver_form.html"