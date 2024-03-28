from django.contrib import admin
from django.urls import path

from core.views import home
import os

admin_path = os.getenv("ADMIN_PATH", "supersecretadmin")
urlpatterns = [path(admin_path, admin.site.urls), path("", home, name="home")]
