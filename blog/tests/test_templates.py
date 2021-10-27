from datetime import datetime
from bs4 import BeautifulSoup
from django.test import TestCase
from blog.models import Blog


# class HomeTemplateTests(TestCase):
#     def setUp(self):
#         lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
#         lorem_ipsum += "Sed non risus. "
#         lorem_ipsum += "Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, "
#         lorem_ipsum += "ultricies sed, dolor. Cras elementum ultrices diam. "
#         lorem_ipsum += "Maecenas ligula massa, varius a, semper congue, "
#         lorem_ipsum += "euismod non, mi. "
#         self.lorem_ipsum = lorem_ipsum
#         test_date = datetime.strptime("2020-01-16", "%Y-%m-%d").date()
#         Blog.objects.create(  # pylint: disable=no-member
#             title="What's New in Django 3?",
#             date=test_date,
#             text=lorem_ipsum,
#         )
#         test_date = datetime.strptime("2020-01-23", "%Y-%m-%d").date()
#         Blog.objects.create(  # pylint: disable=no-member
#             title="New Post", date=test_date, text="Hey there!"
#         )

#     def test_all_blogs_has_title(self):
#         response = self.client.get("/blog/")
#         soup = BeautifulSoup(response.content, features="html.parser")
#         h1_tags = soup.find_all("h1")
#         self.assertEqual(1, len(h1_tags))
#         self.assertEqual("Blog", h1_tags[0].contents[0])

#     def test_all_blogs_are_counted(self):
#         expected = "Xavier has written 2 blogs"
#         response = self.client.get("/blog/")
#         soup = BeautifulSoup(response.content, features="html.parser")
#         h2_tags = soup.find_all("h2")
#         self.assertEqual(1, len(h2_tags))
#         self.assertEqual(expected, h2_tags[0].contents[0])

#     # TODO implement this test with database to add one blog
#     # def test_all_blogs_are_counted_if_one_is_added(self):
#     #     expected = "Xavier has written 3 blogs"
#     #     self.driver.get("%s%s" % (self.live_server_url, "/blog/"))
#     #     actual_count = self.driver.find_elements(By.TAG_NAME, "h2")
#     #     self.assertEqual(1, len(actual_count))
#     #     self.assertEqual(expected, actual_count[0].get_attribute("innerHTML"))

#     def test_all_blogs_has_one_div_per_blog(self):
#         response = self.client.get("/blog/")
#         soup = BeautifulSoup(response.content, features="html.parser")
#         div_tags = soup.find_all("div")
#         blogs = [div for div in div_tags if div["title"] == "blog"]
#         self.assertEqual(2, len(blogs))

#     def test_first_blog_content(self):
#         response = self.client.get("/blog/")
#         soup = BeautifulSoup(response.content, features="html.parser")
#         div_tags = soup.find_all("div")
#         blogs = [div for div in div_tags if div["title"] == "blog"]
#         first_blog = blogs[0]
#         self.assertEqual(1, len(first_blog.find_all(string="New Post")))
#         self.assertEqual(1, len(first_blog.find_all(string="JAN 23 2020")))
#         self.assertEqual(1, len(first_blog.find_all(string="Hey there!")))

#     def test_second_blog_content(self):
#         response = self.client.get("/blog/")
#         soup = BeautifulSoup(response.content, features="html.parser")
#         div_tags = soup.find_all("div")
#         blogs = [div for div in div_tags if div["title"] == "blog"]
#         second_blog = blogs[1]
#         self.assertEqual(1, len(second_blog.find_all(string="What's New in Django 3?")))
#         self.assertEqual(1, len(second_blog.find_all(string="JAN 16 2020")))
#         self.assertEqual(1, len(second_blog.find_all(string=self.lorem_ipsum)))
