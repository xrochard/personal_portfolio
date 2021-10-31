from bs4 import BeautifulSoup
from django.test import TestCase
from blog.models import Blog


class BlogsTemplateTests(TestCase):
    def setUp(self):
        response = self.client.get("/blog/")
        self.soup = BeautifulSoup(response.content, features="html.parser")

    def test_holds_blog_title(self):
        h1_tags = self.soup.find_all("h1")
        self.assertEqual(1, len(h1_tags))
        self.assertEqual("Blog", h1_tags[0].contents[0])

    def test_show_zero_as_the_number_of_blogs(self):
        h2_tags = self.soup.find_all("h2")
        self.assertEqual(1, len(h2_tags))
        self.assertEqual("Xavier has written 0 blogs.", h2_tags[0].contents[0])


class BlogsTemplateWithOneBlogTests(TestCase):
    fixtures = ["one_blog.json"]

    def test_show_one_as_the_number_of_blogs(self):
        response = self.client.get("/blog/")
        soup = BeautifulSoup(response.content, features="html.parser")
        h2_tags = soup.find_all("h2")
        self.assertEqual(1, len(h2_tags))
        self.assertEqual("Xavier has written 1 blogs.", h2_tags[0].contents[0])


# to run the tests on command line
# python ./manage.py test blog.tests.test_views
#
