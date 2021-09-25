from django.test import SimpleTestCase


class HomePageTest(SimpleTestCase):
    def test_200_Response_with_home_template(self):
        with self.assertTemplateUsed("home.html"):
            response = self.client.get("")
            self.assertEqual(response.status_code, 200)
