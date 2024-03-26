from django.shortcuts import render
from things.models import Thing


def home(request):
    things = Thing.objects.all()

    return render(request, "core/home.html", {"things": things})
