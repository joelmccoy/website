from experience.models import Job, Degree
import json
import os


def run():
    with open(os.path.join(os.path.dirname(__file__), "data_experience.json")) as f:
        experience = json.load(f)

    Job.objects.all().delete()

    for job in experience["jobs"]:
        Job.objects.create(**job)

    Degree.objects.all().delete()

    for degree in experience["degrees"]:
        Degree.objects.create(**degree)
