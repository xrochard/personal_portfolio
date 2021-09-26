from portfolio.models import Project
from django.test import TestCase
from portfolio import views


class HomePageTest(TestCase):
    def test_200_Response_with_home_template(self):
        with self.assertTemplateUsed("home.html"):
            response = self.client.get("")
            self.assertEqual(response.status_code, 200)


class ProjectModelTest(TestCase):
    def test_all_projects_gets_all_projects(self):
        Project.objects.create(title="project_1")  # pylint: disable=no-member
        Project.objects.create(title="project_2")  # pylint: disable=no-member
        result = views.all_projects()
        self.assertEqual(2, len(result))
