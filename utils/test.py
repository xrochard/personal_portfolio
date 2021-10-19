import unittest
from utils.coverage_parser import file_coverage_parser


class CoverageParserTest(unittest.TestCase):
    def test_positive_file_coverage_parser(self):
        positive_file = "Name                  Stmts   Miss  Cover\n"
        positive_file += "-----------------------------------------\n"
        positive_file += "blog\\models.py            6      0   100%\n"
        positive_file += "blog\\urls.py              3      0   100%\n"
        positive_file += "-----------------------------------------\n"
        positive_file += "TOTAL                    52      0   100%\n"
        error_raised = False
        try:
            file_coverage_parser(file=positive_file, debug=True)
        except ValueError:
            error_raised = True
        self.assertFalse(error_raised)

    def test_negative_file_coverage_parser(self):
        positive_file = "Name                  Stmts   Miss  Cover\n"
        positive_file += "-----------------------------------------\n"
        positive_file += "blog\\models.py            6      0   100%\n"
        positive_file += "blog\\urls.py              3      0   80%\n"
        positive_file += "-----------------------------------------\n"
        positive_file += "TOTAL                    52      0   100%\n"
        error_raised = False
        try:
            file_coverage_parser(file=positive_file, debug=True)
        except ValueError as error_message:
            error_raised = True
            line_detected = error_message
        self.assertTrue(error_raised)
        self.assertEqual("blog\\urls.py: 80%", line_detected.__str__())


if __name__ == "__main__":
    unittest.main()
