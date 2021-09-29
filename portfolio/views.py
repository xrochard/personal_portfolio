from django.shortcuts import render
from .models import Project


def all_projects():
    return Project.objects.all()  # pylint: disable=no-member


def home(request):
    projects = all_projects()
    return render(request, "home.html", {"projects": projects})
