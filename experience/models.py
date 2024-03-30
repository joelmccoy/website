from django.db import models
from django.contrib.postgres.fields import ArrayField


class Job(models.Model):
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    tagline = models.TextField()
    tags = ArrayField(models.CharField(max_length=200))
    start_month = models.IntegerField()
    end_month = models.IntegerField()
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.company} - {self.title}"


class Degree(models.Model):
    institution = models.CharField(max_length=200)
    degree_name = models.CharField(max_length=200)
    completion_month = models.IntegerField()
    completion_year = models.IntegerField()

    def __str__(self):
        return f"{self.institution} - {self.degree}"
