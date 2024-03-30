from django.contrib import admin

# Register your models here.
from .models import Job, Degree

admin.site.register(Job)
admin.site.register(Degree)
