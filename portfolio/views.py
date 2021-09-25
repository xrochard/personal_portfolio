from django.shortcuts import render
from django.http import HttpResponse
import portfolio


def home(request):
    return render(request, "home.html")