from django.contrib import admin
from django.urls import path

from core.views import home, about, experience, skills, projects, contact
import os

admin_path = os.getenv("ADMIN_PATH", "supersecretadmin")
urlpatterns = [
    path(admin_path, admin.site.urls),
    path("", home, name="home"),
    path("home", home, name="home"),
    path("about", about, name="about"),
    path("experience", experience, name="experience"),
    path("skills", skills, name="skills"),
    path("projects", projects, name="projects"),
    path("contact", contact, name="contact"),
]
