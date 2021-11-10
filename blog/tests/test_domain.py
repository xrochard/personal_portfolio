from datetime import datetime
import unittest
from blog.domain import blog_handling


class FormatterTest(unittest.TestCase):
    def test_date_formatting(self):
        test_date = datetime.strptime("2020-01-16", "%Y-%m-%d").date()
        test_data = [{"title": "test_title", "text": "test_text", "date": test_date}]
        expected_data = []
        expected_data = [
            {key: value for key, value in entry.items()} for entry in test_data
        ]
        expected_data[0]["date"] = "2020-01-16"
        self.assertEqual(blog_handling.date_format(test_data), expected_data)


# to run the tests on command line
# python ./manage.py test blog.tests.test_domain
