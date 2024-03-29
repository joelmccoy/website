from django.shortcuts import render
from things.models import Thing


def home(request):
    things = Thing.objects.all()

    return render(request, "core/home.html", {"things": things})


def about(request):
    return render(request, "core/about.html")


def experience(request):
    return render(request, "core/experience.html")


def skills(request):
    return render(request, "core/skills.html")


def projects(request):
    return render(request, "core/projects.html")


def contact(request):
    return render(request, "core/contact.html")
