import os
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# from portfolio.models import Project


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

    super.title_1 = "New Post"
    super.date_1 = "JAN 23, 2020"
    super.text_1 = "Hey there!"
    super.title_2 = "What's New in Django 3?"
    super.date_2 = "JAN 16, 2020"
    lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    lorem_ipsum += "Sed non risus. "
    lorem_ipsum += "Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, "
    lorem_ipsum += "ultricies sed, dolor. Cras elementum ultrices diam. "
    lorem_ipsum += "Maecenas ligula massa, varius a, semper congue, euismod non, mi. "
    lorem_ipsum += "Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, "
    lorem_ipsum += "non fermentum diam nisl sit amet erat. Duis semper. "
    lorem_ipsum += "Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. "
    lorem_ipsum += "Pellentesque congue. Ut in risus volutpat libero pharetra tempor. "
    lorem_ipsum += "Cras vestibulum bibendum augue. Praesent egestas leo in pede. "
    lorem_ipsum += "Praesent blandit odio eu enim. "
    lorem_ipsum += "Pellentesque sed dui ut augue blandit sodales. "
    lorem_ipsum += "Vestibulum ante ipsum primis in faucibus orci luctus "
    lorem_ipsum += "et ultrices posuere cubilia Curae; "
    lorem_ipsum += "Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. "
    lorem_ipsum += "Maecenas adipiscing ante non diam sodales hendrerit."
    super.text_2 = lorem_ipsum

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        super(HomeTemplateTests, cls).tearDownClass()

    def test_all_blogs_has_title(self):
        expected = "Blog"
        self.driver.get("%s%s" % (self.live_server_url, "/blog/"))
        actual_titles = self.driver.find_elements(By.TAG_NAME, "h1")
        self.assertEqual(1, len(actual_titles))
        self.assertEqual(expected, actual_titles[0].get_attribute("innerHTML"))

    def test_all_blogs_are_counted(self):
        expected = "Xavier has written 2 blogs"
        self.driver.get("%s%s" % (self.live_server_url, "/blog/"))
        actual_count = self.driver.find_elements(By.TAG_NAME, "h2")
        self.assertEqual(1, len(actual_count))
        self.assertEqual(expected, actual_count[0].get_attribute("innerHTML"))

    # TODO implement this test with database to add one blog
    # def test_all_blogs_are_counted_if_one_is_added(self):
    #     expected = "Xavier has written 3 blogs"
    #     self.driver.get("%s%s" % (self.live_server_url, "/blog/"))
    #     actual_count = self.driver.find_elements(By.TAG_NAME, "h2")
    #     self.assertEqual(1, len(actual_count))
    #     self.assertEqual(expected, actual_count[0].get_attribute("innerHTML"))

    def test_all_blogs_has_one_div_per_blog(self):
        self.driver.get("%s%s" % (self.live_server_url, "/blog/"))
        divs = self.driver.find_elements(By.TAG_NAME, "div")
        rendered_blogs = [div for div in divs if div.get_attribute("title") == "blog"]
        self.assertEqual(2, len(rendered_blogs))

    def test_first_blog_content(self):
        self.driver.get("%s%s" % (self.live_server_url, "/blog/"))
        divs = self.driver.find_elements(By.TAG_NAME, "div")
        blogs = [div for div in divs if div.get_attribute("title") == "blog"]
        first_blog = [
            blog for blog in blogs if blog.get_attribute("title") == super.title_1
        ][0]
        first_blog_content = first_blog.get_attribute("innerHTML")
        self.assertInHTML(super.title_1, first_blog_content)
        self.assertInHTML(super.date_1, first_blog_content)
        self.assertInHTML(super.text_1, first_blog_content)

    def test_second_blog_content(self):
        self.driver.get("%s%s" % (self.live_server_url, "/blog/"))
        divs = self.driver.find_elements(By.TAG_NAME, "div")
        blogs = [div for div in divs if div.get_attribute("title") == "blog"]
        second_blog = [
            blog for blog in blogs if blog.get_attribute("title") == super.title_2
        ][0]
        second_blog_content = second_blog.get_attribute("innerHTML")
        self.assertInHTML(super.title_2, second_blog_content)
        self.assertInHTML(super.date_2, second_blog_content)
        self.assertInHTML(super.text_2, second_blog_content)

    def test_blogs_order(self):
        self.driver.get("%s%s" % (self.live_server_url, "/blog/"))
        divs = self.driver.find_elements(By.TAG_NAME, "div")
        blogs = [div for div in divs if div.get_attribute("title") == "blog"]
        self.assertEqual(super.title_1, blogs[0].get_attribute("title"))
        self.assertEqual(super.title_2, blogs[1].get_attribute("title"))
