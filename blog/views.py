from django.shortcuts import render
from blog.models import Blog


def blog_model_full_query():
    blog_entries = []
    for blog_entry in Blog.objects.all():  # pylint: disable=no-member
        blog_entries.append(
            {
                "title": blog_entry.title,
                "text": blog_entry.text,
            }
        )
    return blog_entries


def from_blog_model_to_blogs():
    return blog_model_full_query()


def blogs(request):
    blog_entries = from_blog_model_to_blogs()
    number = len(blog_entries)
    return render(request, "blogs.html", {"number": number, "blogs": blog_entries})
