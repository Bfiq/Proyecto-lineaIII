from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "centro_educativo"
urlpatterns = [
    path("", LoginView.as_view(template_name='centro_educativo/login.html'), name="login"),
    path("home", views.home, name="home"),
    path("courses", views.courses, name="courses"),
    path("studentForm", views.studentForm, name="studentForm"),
    path("editStudent/<int:student_id>", views.editStudent, name="editStudent"),
    path("editCourse/<int:course_id>", views.editCourse, name="editCourse"),
    path("editRecordCourse", views.editRecordCourse, name="editRecordCourse"),
    path("deleteStudent/<int:pk>", views.deleteStudent, name="deleteStudent"),
    path("deleteCourse/<int:pk>", views.deleteCourse, name="deleteCourse"),
    path("logout", LogoutView.as_view(template_name='centro_educativo/login.html'), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""path("register", views.register, name="register"),"""