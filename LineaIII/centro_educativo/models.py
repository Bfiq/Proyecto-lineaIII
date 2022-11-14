from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=30)
    credits = models.BigIntegerField()

    def __str__(self):
        return self.name

class Students(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    courses = models.ManyToManyField(Courses, through='StudentsCourses')

    def __str__(self):
        return self.name

class Roles(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)

class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rol_id = models.ForeignKey(Roles, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class StudentsCourses(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE) 
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

#modal with django