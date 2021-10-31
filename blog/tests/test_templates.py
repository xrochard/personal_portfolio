from bs4 import BeautifulSoup
from django.test import TestCase


class BlogsTemplateTests(TestCase):
    def test_holds_Blog_title(self):
        response = self.client.get("/blog/")
        soup = BeautifulSoup(response.content, features="html.parser")
        h1_tags = soup.find_all("h1")
        self.assertEqual(1, len(h1_tags))
        self.assertEqual("Blog", h1_tags[0].contents[0])


# to run the tests on command line
# python ./manage.py test blog.tests.test_views
#
