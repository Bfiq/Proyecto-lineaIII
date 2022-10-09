from django.db import models
from django.contrib.auth.models import User

class Students(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)

class Courses(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=30)
    credits = models.BigIntegerField()
    students = models.ManyToManyField(Students)

    def __str__(self):
        return self.name

class Roles(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rol_id = models.ForeignKey(Roles, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rol_id

#modal with django