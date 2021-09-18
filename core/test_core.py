from django.test import TestCase


class SimpleSanityTest(TestCase):
    def test_details(self):
        response = self.client.get("/admin/")
        # return code 302 indicate redirection (request page to connect as an identified user)
        self.assertEqual(response.status_code, 302)
