from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

app_name = "centro_educativo"
urlpatterns = [
    path("", LoginView.as_view(template_name='centro_educativo/login.html'), name="login")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""path("users", views.users, name="users"),
    path("register", views.register, name="register"),
    path("logout", LogoutView.as_view(template_name='app1/index.html'), name="logout"),
    path("modelbd", views.modelbd, name="modelbd"),"""