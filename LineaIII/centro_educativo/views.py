from unicodedata import name
from django.shortcuts import get_object_or_404, redirect, render
from .models import Students, Users, Courses#, StudentsCourses
from django.db.models import Q

def home(request):
    students_list = Students.objects.all()
    courses_list = Courses.objects.all()

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
        return render(request, "centro_educativo/home.html", {"students_list": students_list,"courses_list":courses_list, "user_rol":user_rol})
    else:
        return render(request, "centro_educativo/home.html")

def courses(request):
    courses_list = Courses.objects.all()

    queryset = request.GET.get("buscar") #si existe?

    if queryset:#if request.GET.get("buscar")
        courses_list = Courses.objects.filter(
            Q(code__icontains=queryset) |
            Q(name__icontains=queryset) |
            Q(credits__icontains=queryset) 
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
        return render(request, "centro_educativo/courses.html", {"courses_list": courses_list, "user_rol":user_rol})
    else:
        return render(request, "centro_educativo/courses.html")

#eliminar?
def studentForm(request):
    if(request.method == "POST"):
        if request.POST["studentCode"]:
            code = request.POST["studentCode"]
            name = request.POST["studentName"]
            lastName = request.POST["studentLastName"]
            newStudent = Students(code=code,name=name,lastName=lastName)
            newStudent.save()

    return redirect('/home')

""" def editStudent(request,student_id):
    student = Students.objects.filter(id=student_id).first() """

def editStudent(request,student_id):
    courses_list = Courses.objects.all()
    student = Students.objects.filter(id=student_id).first()
    data = {
        'title' : 'Edición del alumno',
        'student' :  student,
        "courses_list": courses_list
    }

    return render(request, "centro_educativo/editStudent.html", data)

def editRecordStudent(request):
    if(request.method == "POST"):
        if request.POST["studentCode"]:
            id = request.POST["id"]
            code = request.POST["studentCode"]
            name = request.POST["studentName"]
            lastName = request.POST["studentLastName"]
            student = Students.objects.get(id=id)
            student.name = name
            student.code = code
            student.lastName = lastName
            student.save()

    return redirect('/home')


def addCourseinUser(request, student_id, course_id):
    if student_id:
        #print(f"testeo:{student_id}/{course_id}")#agregar esto a la tabla intermedia
        student = Students.objects.filter(id=student_id).first()
        course = Courses.objects.filter(id=course_id).first()
        """ newStudentsCourses = StudentsCourses(student_id,course_id)
        newStudentsCourses.save() """
        return redirect(f'/editStudent/{student_id}')
    else:
        return redirect('/home')

def editCourse(request,course_id):
    course = Courses.objects.filter(id=course_id).first()
    data = {
        'title' : 'Edición del curso',
        'course' :  course
    }

    return render(request, "centro_educativo/editCourse.html", data)

def editRecordCourse(request):
    if(request.method == "POST"):
        if request.POST["courseCode"]:
            id = request.POST["id"]
            code = request.POST["courseCode"]
            name = request.POST["courseName"]
            credits = request.POST["courseCredits"]
            course = Courses.objects.get(id=id)
            course.name = name
            course.code = code
            course.credits = credits
            course.save()

            return redirect('/courses')

def deleteStudent(request, pk):
    if(pk != ""):
        try:
            """ delStudent = get_object_or_404(Students, pk) """#Revisar
            delStudent = Students.objects.get(pk=pk)
            delStudent.delete()
        except ValueError:
            print(ValueError)

    return redirect('/home')

def deleteCourse(request, pk):
    if(pk != ""):
        try:
            delStudent = Courses.objects.get(pk=pk)
            delStudent.delete()
        except ValueError:
            print(ValueError)

    return redirect('/courses')

def not_found_page(request,exception):
    return render(request,"centro_educativo/404.html",{})
