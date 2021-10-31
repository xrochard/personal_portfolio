from django.test import TestCase
from blog.models import Blog


class BlogModelTestCase(TestCase):
    def test_blog_has_mandatory_default_fields(self):
        test_title = "Blog title"
        test_blog = Blog.objects.create(title=test_title)  # pylint:disable=no-member
        self.assertEqual(test_title, test_blog.title)
        self.assertEqual("", test_blog.text)
        self.assertIsNotNone(test_blog.date)
