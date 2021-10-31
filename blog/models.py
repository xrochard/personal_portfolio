from datetime import date
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, default="Empty title")
    text = models.CharField(max_length=1000, default="")
    date = models.DateField(default=date.today)
