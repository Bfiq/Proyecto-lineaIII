from distutils.log import error
from django.shortcuts import render
from .models import Students, Users

def home(request):
    students_list = Students.objects.all()
    if(request.user.id):
        userid = request.user.id
        user_rol = Users.objects.get(pk=userid) 
        return render(request, "centro_educativo/home.html", {"students_list": students_list, "user_rol":user_rol})

    #print(f"usuario: {userid} rol: {user_rol.rol_id}")


def not_found_page(request,exception):
    return render(request,"centro_educativo/404.html",{})

    #como ver si exite una variable en python?