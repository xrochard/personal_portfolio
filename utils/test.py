"""To run the test do: python -m unittest discover utils"""
from io import StringIO
import unittest
from unittest.mock import patch, mock_open
from utils.coverage_parser import file_coverage_parser, whole_coverage_parser


TOP = "Name                  Stmts   Miss  Cover\n"
TOP += "-----------------------------------------\n"
TOP += "blog\\models.py            6      0   100%\n"
POSITIVE_LINE = "blog\\urls.py              3      0   100%\n"
NEGATIVE_LINE = "blog\\urls.py              3      0   80%\n"
BOTTOM_SEPARATOR = "-----------------------------------------\n"
POSITIVE_BOTTOM = "TOTAL                    52      0   100%\n"
NEGATIVE_BOTTOM = "TOTAL                    52      0   80%\n"
POSITIVE_FILE = TOP + POSITIVE_LINE + BOTTOM_SEPARATOR + POSITIVE_BOTTOM
NEGATIVE_FILE = TOP + NEGATIVE_LINE + BOTTOM_SEPARATOR + POSITIVE_BOTTOM
NEGATIVE_WHOLE = TOP + POSITIVE_LINE + BOTTOM_SEPARATOR + NEGATIVE_BOTTOM


class CoverageParserTest(unittest.TestCase):

    # mock_open is part of thhe mock framework
    # mock stdout to ctach what print() produces
    # the names of the mocks (mock_file, mock_stdout) are defined with the variable in the test call
    # Be aware of the order of the variables: it is the opposite order of the patch decorators
    @patch("builtins.open", new_callable=mock_open, read_data=POSITIVE_FILE)
    @patch("sys.stdout", new_callable=StringIO)
    def test_positive_file_coverage_parser(self, mock_stdout, mock_file):
        file_coverage_parser(file=mock_file)
        self.assertEqual("true\n", mock_stdout.getvalue())

    @patch("builtins.open", new_callable=mock_open, read_data=NEGATIVE_FILE)
    @patch("sys.stdout", new_callable=StringIO)
    def test_negative_file_coverage_parser(self, mock_stdout, mock_file):
        file_coverage_parser(file=mock_file)
        self.assertEqual("blog\\urls.py: 80%\n", mock_stdout.getvalue())

    @patch("builtins.open", new_callable=mock_open, read_data=POSITIVE_FILE)
    @patch("sys.stdout", new_callable=StringIO)
    def test_positive_whole_coverage_parser(self, mock_stdout, mock_file):
        whole_coverage_parser(file=mock_file)
        self.assertEqual("true\n", mock_stdout.getvalue())

    @patch("builtins.open", new_callable=mock_open, read_data=NEGATIVE_WHOLE)
    @patch("sys.stdout", new_callable=StringIO)
    def test_negative_whole_coverage_parser(self, mock_stdout, mock_file):
        whole_coverage_parser(file=mock_file)
        self.assertEqual("whole coverage: 80%\n", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
