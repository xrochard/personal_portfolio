from datetime import datetime
import unittest
from blog.domain import blog_handling


class FormatterTest(unittest.TestCase):
    def test_date_formatting(self):
        test_data = [
            {
                "title": "test_title",
                "text": "test_text",
                "date": datetime.strptime("2020-01-16", "%Y-%m-%d").date(),
            },
            {
                "title": "test_title",
                "text": "test_text",
                "date": datetime.strptime("2020-03-18", "%Y-%m-%d").date(),
            },
            {
                "title": "test_title",
                "text": "test_text",
                "date": datetime.strptime("2020-07-1", "%Y-%m-%d").date(),
            },
        ]
        expected_data = []
        expected_data = [
            {key: value for key, value in entry.items()} for entry in test_data
        ]
        expected_data[0]["date"] = "2020 JAN 16"
        expected_data[1]["date"] = "2020 MAR 18"
        expected_data[2]["date"] = "2020 JUL 1"
        self.assertEqual(blog_handling.date_format(test_data), expected_data)


# to run the tests on command line
# python ./manage.py test blog.tests.test_domain
