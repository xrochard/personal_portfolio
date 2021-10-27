from datetime import datetime
from django.test import TestCase
from blog.models import Blog
from blog import views


# class BlogPageTest(TestCase):
#     def test_calls_to_blog_url_are_redirected(self):
#         response = self.client.get("/blog")
#         # 301 means perment redirection
#         self.assertEqual(response.status_code, 301)

#     def test_200_response_with_all_template(self):
#         with self.assertTemplateUsed("all_blogs.html"):
#             response = self.client.get("/blog/")
#             self.assertEqual(response.status_code, 200)


# class BloqQueryTest(TestCase):
#     def setUp(self):
#         lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
#         lorem_ipsum += "Sed non risus. "
#         lorem_ipsum += "Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, "
#         lorem_ipsum += "ultricies sed, dolor. Cras elementum ultrices diam. "
#         lorem_ipsum += "Maecenas ligula massa, varius a, semper congue, "
#         lorem_ipsum += "euismod non, mi. "
#         self.lorem_ipsum = lorem_ipsum
#         test_date = datetime.strptime("2020-01-16", "%Y-%m-%d").date()
#         Blog.objects.create(  # pylint: disable=no-member
#             title="What's New in Django 3?",
#             date=test_date,
#             text=lorem_ipsum,
#         )

#         test_date = datetime.strptime("2020-01-23", "%Y-%m-%d").date()
#         Blog.objects.create(  # pylint: disable=no-member
#             title="New Post", date=test_date, text="Hey there!"
#         )

#     def test_model_blog_query_all(self):
#         test_date_0 = datetime.strptime("2020-01-16", "%Y-%m-%d").date()
#         test_date_1 = datetime.strptime("2020-01-23", "%Y-%m-%d").date()
#         expected = [
#             {
#                 "title": "What's New in Django 3?",
#                 "date": test_date_0,
#                 "text": self.lorem_ipsum,
#             },
#             {"title": "New Post", "date": test_date_1, "text": "Hey there!"},
#         ]
#         result = views.model_blog_query_all()
#         self.assertEqual(expected, result)

#     def test_all_blogs_sorts_antichronologically(self):
#         self.fail("test")

#     def test_all_blogs_converts_dates(self):
#         self.fail("future test")
