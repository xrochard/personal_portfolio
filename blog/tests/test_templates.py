from bs4 import BeautifulSoup
from django.test import TestCase

# from portfolio.models import Project


class HomeTemplateTests(TestCase):
    def setUp(self):
        self.title_1 = "New Post"
        self.date_1 = "JAN 23, 2020"
        self.text_1 = "Hey there!"
        self.title_2 = "What's New in Django 3?"
        self.date_2 = "JAN 16, 2020"
        lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        lorem_ipsum += "Sed non risus. "
        lorem_ipsum += "Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, "
        lorem_ipsum += "ultricies sed, dolor. Cras elementum ultrices diam. "
        lorem_ipsum += "Maecenas ligula massa, varius a, semper congue, "
        lorem_ipsum += "euismod non, mi. "
        lorem_ipsum += "Proin porttitor, orci nec nonummy molestie, "
        lorem_ipsum += "enim est eleifend mi, "
        lorem_ipsum += "non fermentum diam nisl sit amet erat. Duis semper. "
        lorem_ipsum += "Duis arcu massa, scelerisque vitae, consequat in, "
        lorem_ipsum += "pretium a, enim. "
        lorem_ipsum += "Pellentesque congue. Ut in risus volutpat "
        lorem_ipsum += "libero pharetra tempor. "
        lorem_ipsum += "Cras vestibulum bibendum augue. Praesent egestas leo in pede. "
        lorem_ipsum += "Praesent blandit odio eu enim. "
        lorem_ipsum += "Pellentesque sed dui ut augue blandit sodales. "
        lorem_ipsum += "Vestibulum ante ipsum primis in faucibus orci luctus "
        lorem_ipsum += "et ultrices posuere cubilia Curae; "
        lorem_ipsum += "Aliquam nibh. Mauris ac mauris sed pede "
        lorem_ipsum += "pellentesque fermentum. "
        lorem_ipsum += "Maecenas adipiscing ante non diam sodales hendrerit."
        self.text_2 = lorem_ipsum

    def test_all_blogs_has_title(self):
        response = self.client.get("/blog/")
        soup = BeautifulSoup(response.content, features="html.parser")
        h1_tags = soup.find_all("h1")
        self.assertEqual(1, len(h1_tags))
        self.assertEqual("Blog", h1_tags[0].contents[0])

    def test_all_blogs_are_counted(self):
        expected = "Xavier has written 2 blogs"
        response = self.client.get("/blog/")
        soup = BeautifulSoup(response.content, features="html.parser")
        h2_tags = soup.find_all("h2")
        self.assertEqual(1, len(h2_tags))
        self.assertEqual(expected, h2_tags[0].contents[0])

    # TODO implement this test with database to add one blog
    # def test_all_blogs_are_counted_if_one_is_added(self):
    #     expected = "Xavier has written 3 blogs"
    #     self.driver.get("%s%s" % (self.live_server_url, "/blog/"))
    #     actual_count = self.driver.find_elements(By.TAG_NAME, "h2")
    #     self.assertEqual(1, len(actual_count))
    #     self.assertEqual(expected, actual_count[0].get_attribute("innerHTML"))

    def test_all_blogs_has_one_div_per_blog(self):
        response = self.client.get("/blog/")
        soup = BeautifulSoup(response.content, features="html.parser")
        div_tags = soup.find_all("div")
        blogs = [div for div in div_tags if div["title"] == "blog"]
        self.assertEqual(2, len(blogs))

    def test_first_blog_content(self):
        response = self.client.get("/blog/")
        soup = BeautifulSoup(response.content, features="html.parser")
        div_tags = soup.find_all("div")
        blogs = [div for div in div_tags if div["title"] == "blog"]
        first_blog = blogs[0]
        self.assertEqual(1, len(first_blog.find_all(string=self.title_1)))
        self.assertEqual(1, len(first_blog.find_all(string=self.date_1)))
        self.assertEqual(1, len(first_blog.find_all(string=self.text_1)))

    def test_second_blog_content(self):
        response = self.client.get("/blog/")
        soup = BeautifulSoup(response.content, features="html.parser")
        div_tags = soup.find_all("div")
        blogs = [div for div in div_tags if div["title"] == "blog"]
        second_blog = blogs[1]
        self.assertEqual(1, len(second_blog.find_all(string=self.title_2)))
        self.assertEqual(1, len(second_blog.find_all(string=self.date_2)))
        self.assertEqual(1, len(second_blog.find_all(string=self.text_2)))
