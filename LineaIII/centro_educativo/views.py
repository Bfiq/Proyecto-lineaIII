from django.shortcuts import render
from .models import Students

def home(request):
    students_list = Students.objects.all()
    return render(request, "centro_educativo/home.html", {"students_list": students_list})

def not_found_page(request,exception):
    return render(request,"centro_educativo/404.html",{})