from projects.models import Project
import json
import os


def run():
    with open(os.path.join(os.path.dirname(__file__), "data_projects.json")) as f:
        projects = json.load(f)

    Project.objects.all().delete()

    for project in projects:
        Project.objects.create(**project)
