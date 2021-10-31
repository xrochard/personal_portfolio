from django.test import TestCase
from blog import views


class BlogURLTest(TestCase):
    def test_url_blog_redirection(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_blogs_template_is_called(self):
        with self.assertTemplateUsed("blogs.html"):
            response = self.client.get("/blog/")
            self.assertEqual(response.status_code, 200)


class BlogModelFullQuery(TestCase):
    fixtures = ["one_blog.json"]

    def test_dummy(self):
        test_entries = views.blog_model_full_query()
        self.assertEqual(1, len(test_entries))


# to run the tests on command line
# python ./manage.py test blog.tests.test_views
#
# the first test "test_url_blog_redirection" tests that the http://localhost:8000/blog/ calls something
# the second test "test_blogs_template_is_called" tests that the http://localhost:8000/blog/ calls the blogs.html template
# the tests about the content of the templates is in the test_templates.py module
