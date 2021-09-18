from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, default="Empty title")
