from unicodedata import name
from django.shortcuts import redirect, render
from .models import Students, Users, Courses
from django.db.models import Q

def home(request):
    students_list = Students.objects.all()

    queryset = request.GET.get("buscar") #si existe?

    if queryset:
        students_list = Students.objects.filter(
            Q(code__icontains=queryset) |
            Q(name__icontains=queryset) |
            Q(lastName__icontains=queryset) 
        ).distinct()

    if(request.method == "POST"):
        try:
            if request.POST["courseCode"]:
                courseCode = request.POST["courseCode"]
                courseName = request.POST["courseName"]
                courseCredits = request.POST["courseCredits"]
                print(f"Codigo del curso: {courseCode, courseName, courseCredits}")

                newCourse = Courses(code=courseCode,name=courseName,credits=courseCredits)
                newCourse.save()
            else: pass
        except ValueError:
            print("Error")

    if(request.user.id):
        userid = request.user.id
        user_rol = Users.objects.get(pk=userid) 
        return render(request, "centro_educativo/home.html", {"students_list": students_list, "user_rol":user_rol})
    else:
        return render(request, "centro_educativo/home.html")

def studentForm(request):
    if(request.method == "POST"):
        if request.POST["studentCode"]:
            code = request.POST["studentCode"]
            name = request.POST["studentName"]
            lastName = request.POST["studentLastName"]
            newStudent = Students(code=code,name=name,lastName=lastName)
            newStudent.save()

    return redirect('/home')

def not_found_page(request,exception):
    return render(request,"centro_educativo/404.html",{})

    #como ver si exite una variable en python?