from django.shortcuts import render
from .models import Project


def all_projects():
    return Project.objects.all()  # pylint: disable=no-member


def home(request):
    projects = all_projects()
    rendered = []
    for project in projects:
        rendered.append({"id": project.title + "_id", "title": project.title})
    return render(request, "home.html", {"projects": rendered})
