from datetime import date
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, default="Empty title")
    text = models.TextField(default="")
    date = models.DateField(default=date.today)
