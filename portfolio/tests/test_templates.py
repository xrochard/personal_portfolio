from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os
from portfolio.models import Project


class HomeTemplateTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(HomeTemplateTests, cls).setUpClass()
        options = Options()
        options.headless = True
        if os.name == "nt":
            driver_exe = "utils/geckodriver.exe"
        else:
            driver_exe = "utils/geckodriver"
        cls.driver = webdriver.Firefox(
            options=options, executable_path=driver_exe, service_log_path=os.devnull
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        super(HomeTemplateTests, cls).tearDownClass()

        # Project.objects.create(  # pylint: disable=no-member
        #     title="project_1",
        #     description="project_1_description",
        #     url="http://url_to_project_1/",
        #     image="portfolio/images/pal_gwang.png",
        # )
        # Project.objects.create(  # pylint: disable=no-member
        #     title="project_2",
        #     description="project_2_description",
        #     image="portfolio/images/pal_gwang.png",
        # )

    # Je veux tester que:
    #   - la page contient le titre des deux projets
    #   - la page contient la description des deux projets
    #   - la page contient l'image des deux projets
    #   - la page contient l'URL du premier projet
    #   - le bloc (?) du second projet ne contient pas d'URL
    def test_home_has_one_div_per_project_with_two(self):
        Project.objects.create(title="project_1")  # pylint: disable=no-member
        Project.objects.create(title="project_2")  # pylint: disable=no-member
        self.driver.get("%s%s" % (self.live_server_url, ""))
        divs = self.driver.find_elements(By.TAG_NAME, "div")
        rendered_projects = [
            div
            for div in divs
            if div.get_attribute("id") == "project_1"
            or div.get_attribute("id") == "project_2"
        ]
        self.assertEqual(2, len(rendered_projects))

    def test_home_has_one_div_per_project_with_one(self):
        Project.objects.create(title="project")  # pylint: disable=no-member
        self.driver.get("%s%s" % (self.live_server_url, ""))
        divs = self.driver.find_elements(By.TAG_NAME, "div")
        rendered_projects = [
            div for div in divs if div.get_attribute("id") == "project"
        ]
        self.assertEqual(1, len(rendered_projects))

    def test_home_has_title_in_project_div(self):
        test_title = "title_of_the_test_project"
        Project.objects.create(title=test_title)  # pylint: disable=no-member
        self.driver.get("%s%s" % (self.live_server_url, ""))
        divs = self.driver.find_elements(By.TAG_NAME, "div")
        rendered_projects = [
            div for div in divs if div.get_attribute("id") == test_title
        ]
        result = rendered_projects[0].get_attribute("innerHTML")
        self.assertInHTML(test_title, result, count=1)
