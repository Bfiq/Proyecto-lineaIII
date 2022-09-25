from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "centro_educativo"
urlpatterns = [
    path("", LoginView.as_view(template_name='centro_educativo/login.html'), name="login"),
    path("home", views.home, name="home"),
    path("logout", LogoutView.as_view(template_name='centro_educativo/login.html'), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
    path("register", views.register, name="register"),
    path("modelbd", views.modelbd, name="modelbd"),"""