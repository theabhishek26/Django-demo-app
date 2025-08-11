from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    context={
            "joining_date":"10 Aug 2025",
            "current_year": datetime.datetime.now().year,
        }
    return render(request, "hello/home.html", context)
