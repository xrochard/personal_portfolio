import unittest
from django.test import Client


class BlogPageTest(unittest.TestCase):
    def test_url_blog_redirection(self):
        client = Client()
        response = client.get("/blog/")
        self.assertEqual(200, response.status_code)


if __name__ == "__main__":
    unittest.main()

# to run the tests on command line
# python ./manage.py test blog.tests.test_views
