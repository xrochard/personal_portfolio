import json
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


class BlogModelFullQueryOneBasicBlog(TestCase):
    fixtures = ["one_blog.json"]

    def test_returns_one_blog_with_fields(self):
        with open("./blog/fixtures/one_blog.json", encoding="utf-8") as json_fixtures:
            fixtures_list = json.load(json_fixtures)
        expected_entries = [
            json_entry["fields"]
            for json_entry in fixtures_list
            if json_entry["model"] == "blog.Blog"
        ]
        for entry in expected_entries:
            entry["text"] = ""

        actual_entries = views.blog_model_full_query()
        self.assertListEqual(actual_entries, expected_entries)


class BlogModelFullQueryThreeBlogs(TestCase):
    fixtures = ["three_blogs.json"]

    def test_returns_three_blogs_with_fields(self):
        with open(
            "./blog/fixtures/three_blogs.json", encoding="utf-8"
        ) as json_fixtures:
            fixtures_list = json.load(json_fixtures)

        expected_entries = [
            json_entry["fields"]
            for json_entry in fixtures_list
            if json_entry["model"] == "blog.Blog"
        ]

        actual_entries = views.blog_model_full_query()
        self.assertListEqual(actual_entries, expected_entries)


# to run the tests on command line
# python ./manage.py test blog.tests.test_views
#
# About the tests of BlogURLTest class:
# The first test "test_url_blog_redirection" tests that
# the http://localhost:8000/blog/ calls something.
# The second test "test_blogs_template_is_called" tests that
# the http://localhost:8000/blog/ calls the blogs.html template
# The tests about the content of the templates is in the test_templates.py module
