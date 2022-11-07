import imp
from django.contrib import admin
from .models import Roles, Courses,Users, Students, StudentsCourses

admin.site.register(Roles)
admin.site.register(Courses)
admin.site.register(Users)
admin.site.register(Students)
admin.site.register(StudentsCourses)