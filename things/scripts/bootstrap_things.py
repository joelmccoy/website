from things.models import Thing
import json
import os


def run():
    with open(os.path.join(os.path.dirname(__file__), "data_things.json")) as f:
        things = json.load(f)

    # First, delete all the things
    Thing.objects.all().delete()

    for thing in things:
        Thing.objects.create(**thing)
