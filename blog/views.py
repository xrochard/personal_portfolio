from django.shortcuts import render
from .models import Blog


def model_blog_query_all():
    blogs = []
    for blog in Blog.objects.all():  # pylint: disable=no-member
        blogs.append({"title": blog.title, "date": blog.date, "text": blog.text})
    return blogs


def all_blogs(request):
    blogs = model_blog_query_all()
    return render(request, "all_blogs.html", {"blogs": blogs})
