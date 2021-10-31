import unittest
from django.test import Client


class BlogPageTest(unittest.TestCase):
    def test_url_blog_redirection(self):
        client = Client()
        response = client.get("/blog/")
        self.assertEqual(200, response.status_code)

    # def test_all_blogs_template_is_called(self):
    #     self.fail("writing in progrress")


if __name__ == "__main__":
    unittest.main()

# to run the tests on command line
# python ./manage.py test blog.tests.test_views
#
# the first test "test_url_blog_redirection" tests that the http://localhost:8000/blog/ calls something
# the second test "test_blogs_template_is_called" tests that the http://localhost:8000/blog/ calls the blogs.html template
# the tests about the content of the templates is in the test_templates.py module
