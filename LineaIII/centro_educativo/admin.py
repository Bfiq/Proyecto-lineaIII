import imp
from django.contrib import admin
from .models import Roles, Courses,Users, Students

admin.site.register(Roles)
admin.site.register(Courses)
admin.site.register(Users)
admin.site.register(Students)