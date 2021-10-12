from django.test import TestCase


class BlogPageTest(TestCase):
    def test_calls_to_blog_url_are_redirected(self):
        response = self.client.get("/blog")
        # 301 means perment redirection
        self.assertEqual(response.status_code, 301)

    def test_200_response_with_all_template(self):
        with self.assertTemplateUsed("all_blogs.html"):
            response = self.client.get("/blog/")
            self.assertEqual(response.status_code, 200)
