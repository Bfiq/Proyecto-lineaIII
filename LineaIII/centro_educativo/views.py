from django.shortcuts import render

def home(request):
    return render(request, "centro_educativo/home.html", {})