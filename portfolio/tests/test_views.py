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

    def test_model_query_gets_all_projects(self):
        result = views.model_project_query_all()
        self.assertEqual(2, len(result))

    def test_model_query_gets_all_projects_empty_fields(self):
        expected = [
            {
                "title": "project_1",
                "description": "",
                "url": "",
                "image": "portfolio/images/pal_gwang.png",
            },
            {
                "title": "project_2",
                "description": "",
                "url": "",
                "image": "portfolio/images/pal_gwang.png",
            },
        ]
        result = views.model_project_query_all()
        for index in range(len(expected)):
            self.assertDictEqual(expected[index], result[index])

    def test_model_query_gets_optional_fields(self):
        Project.objects.create(  # pylint: disable=no-member
            title="project_3", description="description_3", url="http://url_3.com"
        )
        expected = {
            "title": "project_3",
            "description": "description_3",
            "url": "http://url_3.com",
            "image": "portfolio/images/pal_gwang.png",
        }
        result = views.model_project_query_all()[2]
        self.assertDictEqual(expected, result)

    def test_home_context_holds_all_projects(self):
        expected_titles = ["project_1", "project_2"]

        # indicate here the view that is tested
        response = self.client.get(reverse("home"))

        context_projects = response.context["projects"]
        self.assertEqual(len(expected_titles), len(context_projects))
        actual_titles = []
        for project in context_projects:
            actual_titles.append(project["title"])
        self.assertEqual(set(expected_titles), set(actual_titles))
