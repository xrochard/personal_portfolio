import os
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
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

    def test_home_has_description_in_project_div(self):
        test_description = "Description of the test project"
        Project.objects.create(  # pylint: disable=no-member
            title="test", description=test_description
        )
        self.driver.get("%s%s" % (self.live_server_url, ""))
        divs = self.driver.find_elements(By.TAG_NAME, "div")
        rendered_projects = [div for div in divs if div.get_attribute("id") == "test"]
        result = rendered_projects[0].get_attribute("innerHTML")
        self.assertInHTML(test_description, result, count=1)

    def test_home_displays_image_in_project_div(self):
        default_image = "media/portfolio/images/pal_gwang.png"
        Project.objects.create(title="test")  # pylint: disable=no-member
        self.driver.get("%s%s" % (self.live_server_url, ""))
        divs = self.driver.find_elements(By.TAG_NAME, "div")
        rendered_projects = [div for div in divs if div.get_attribute("id") == "test"]
        image_elements = rendered_projects[0].find_elements(By.TAG_NAME, "img")
        result_image = image_elements[0].get_attribute("src")[-len(default_image) :]
        self.assertEqual(default_image, result_image)

    def test_home_displays_link_in_project_div(self):
        test_url = "http://test.com/"
        Project.objects.create(title="test", url=test_url)  # pylint: disable=no-member

        self.driver.get("%s%s" % (self.live_server_url, ""))
        divs = self.driver.find_elements(By.TAG_NAME, "div")
        rendered_projects = [div for div in divs if div.get_attribute("id") == "test"]

        url_elements = rendered_projects[0].find_elements(By.TAG_NAME, "a")
        result_url = url_elements[0].get_attribute("href")
        self.assertEqual(test_url, result_url)

    def test_home_displays_no_link_if_no_url(self):
        Project.objects.create(title="test")  # pylint: disable=no-member

        self.driver.get("%s%s" % (self.live_server_url, ""))
        divs = self.driver.find_elements(By.TAG_NAME, "div")
        rendered_projects = [div for div in divs if div.get_attribute("id") == "test"]

        url_elements = rendered_projects[0].find_elements(By.TAG_NAME, "a")
        self.assertEqual(0, len(url_elements))
