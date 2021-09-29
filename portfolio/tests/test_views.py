from django.http import response
from portfolio.models import Project
from django.test import TestCase
from portfolio import views
from django.urls import reverse


class HomePageTest(TestCase):
    def test_200_Response_with_home_template(self):
        with self.assertTemplateUsed("home.html"):
            response = self.client.get("")
            self.assertEqual(response.status_code, 200)


class ViewsTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(ViewsTest, cls).setUpClass()
        Project.objects.create(title="project_1")  # pylint: disable=no-member
        Project.objects.create(title="project_2")  # pylint: disable=no-member

    def test_all_projects_gets_all_projects(self):
        result = views.all_projects()
        self.assertEqual(2, len(result))

    def test_home_context_holds_all_projects(self):
        expected_titles = ["project_1", "project_2"]

        # indicate here the view that is tested
        response = self.client.get(reverse("home"))

        context_projects = response.context["projects"]
        self.assertEqual(len(expected_titles), len(context_projects))
        actual_titles = []
        for project in context_projects:
            actual_titles.append(project.title)
        self.assertEqual(set(expected_titles), set(actual_titles))
