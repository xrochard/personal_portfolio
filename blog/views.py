from datetime import datetime
from django.shortcuts import render
from blog.domain import data_format
from blog.models import Blog


def blog_model_full_query():
    blog_entries = []
    for blog_entry in Blog.objects.all():  # pylint: disable=no-member
        blog_entries.append(
            {
                "title": blog_entry.title,
                "text": blog_entry.text,
                "date": blog_entry.date,
            }
        )
    return blog_entries


def blogs(request):
    blog_entries = blog_model_full_query()
    blog_entries = data_format.date_format(blog_entries)
    number = len(blog_entries)
    return render(request, "blogs.html", {"number": number, "blogs": blog_entries})
