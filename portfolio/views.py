from django.shortcuts import render
from .models import Project


def model_project_query_all():
    projects = []
    for project in Project.objects.all():  # pylint: disable=no-member
        projects.append(
            {
                "title": project.title,
                "description": project.description,
                "url": project.url,
                "image": project.image,
            }
        )
    return projects


def home(request):
    projects = model_project_query_all()
    return render(request, "home.html", {"projects": projects})
