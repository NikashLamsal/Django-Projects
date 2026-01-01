from django.shortcuts import render

from django.http import HttpResponse
import random
# from django.views import views

def index(request):
    return render(request, "index.html")


def project(request):
    lucky_number = random.randint(0,20)
    context = {"lucky number" : lucky_number}
    return render(request , "project/project.html", context)


