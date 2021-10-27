from datetime import datetime
from django.test import TestCase
from blog.models import Blog


class BlogModelTest(TestCase):
    def test_blog_content(self):
        test_title = "Blog title"
        test_date = datetime.strptime("2021-10-17", "%Y-%m-%d").date()
        test_text = "Blog's text"
        test_blog = Blog.objects.create(  # pylint: disable=no-member
            title=test_title, date=test_date, text=test_text
        )
        self.assertEqual(test_title, test_blog.title)
        self.assertEqual(test_date, test_blog.date)
        self.assertEqual(test_text, test_blog.text)
