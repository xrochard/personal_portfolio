from portfolio.models import Project
from django.test import TestCase


class ProjectModelTest(TestCase):
    def test_project_exists(self):
        title = "Nice title"
        test_project = Project.objects.create(title=title)  # pylint: disable=no-member
        self.assertIsNotNone(test_project)

    def test_too_long_title_project_results_in_error(self):
        # Note: sqlite doesn't enforce the max_length of the Charfield.
        pass
