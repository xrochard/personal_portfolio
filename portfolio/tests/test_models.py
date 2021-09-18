from portfolio.models import Project
from django.test import TestCase
from parameterized import parameterized


class ProjectModelTest(TestCase):
    def test_too_long_title_project_results_in_error(self):
        # Note: sqlite doesn't enforce the max_length of the Charfield.
        pass

    @parameterized.expand(
        [
            ["title", "Nice title"],
            ["description", "Nice description, longer than title"],
            ["url", "http://just_an_url.com"],
            ["image", "protfolio/images/pal_gwang.png"],
        ]
    )
    def test_project_has(self, attribute, value):
        constructor_argument = {attribute: value}
        test_project = Project.objects.create(  # pylint: disable=no-member
            **constructor_argument
        )
        self.assertIsNotNone(test_project)

    def test_project_with_empty_url(self):
        test_project = Project.objects.create()  # pylint: disable=no-member
        self.assertEqual("", test_project.url)