from django.contrib import admin
from django.urls import path

from core.views import home

urlpatterns = [path("supersecretadmin/", admin.site.urls), path("", home, name="home")]
