from core.views import home
from django.contrib import admin
from django.urls import path

urlpatterns = [path("supersecretadmin/", admin.site.urls), path("", home, name="home")]
