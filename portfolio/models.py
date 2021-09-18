from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, default="Empty title")
    description = models.CharField(max_length=250, default="Empty description")
