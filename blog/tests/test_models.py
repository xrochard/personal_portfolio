from datetime import datetime
from django.test import TestCase
from blog.models import Blog

# from parameterized import parameterized


class BlogModelTest(TestCase):

    # @parameterized.expand(
    #     [
    #         ["title", "Nice title"],
    #         ["description", "Nice description, longer than title"],
    #         ["url", "http://just_an_url.com"],
    #         ["image", "protfolio/images/pal_gwang.png"],
    #     ]
    # )
    # def test_project_has(self, attribute, value):
    #     constructor_argument = {attribute: value}
    #     test_project = Project.objects.create(  # pylint: disable=no-member
    #         **constructor_argument
    #     )
    #     self.assertIsNotNone(test_project)

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
