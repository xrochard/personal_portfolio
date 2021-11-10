from datetime import datetime
import unittest
from blog.domain import data_format


class FormatterTest(unittest.TestCase):
    def test_date_formatting(self):
        test_date = datetime.strptime("2020-01-16", "%Y-%m-%d").date()
        test_data = {"title": "test_title", "text": "test_text", "date": test_date}
        expected_data = {}
        for key, value in test_data.items():
            expected_data[key] = value
        expected_data["date"] = "JAN 16 2020"
        self.assertDictEqual(data_format.date_format(test_data), expected_data)


# to run the tests on command line
# python ./manage.py test blog.tests.test_domain
