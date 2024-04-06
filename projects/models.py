from django.db import models
from django.contrib.postgres.fields import ArrayField


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    tags = ArrayField(models.CharField(max_length=200))
    github_link = models.URLField()

    def __str__(self):
        return f"{self.name}"
