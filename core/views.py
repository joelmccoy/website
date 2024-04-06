from django.shortcuts import render
from things.models import Thing
from experience.models import Job, Degree
from projects.models import Project


def home(request):
    things = Thing.objects.all()

    return render(request, "core/home.html", {"things": things})


def about(request):
    return render(request, "core/about.html")


def experience(request):
    jobs = Job.objects.all()
    degrees = Degree.objects.all()
    return render(request, "core/experience.html", {"jobs": jobs, "degrees": degrees})


def skills(request):
    return render(request, "core/skills.html")


def projects(request):
    projects = Project.objects.all()
    return render(request, "core/projects.html", {"projects": projects})


def contact(request):
    return render(request, "core/contact.html")
