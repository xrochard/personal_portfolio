import json
from bs4 import BeautifulSoup
from django.test import TestCase


class BlogExtractor:
    def __init__(self, soup):
        self.blogs = [tag for tag in soup.find_all("div") if tag["title"] == "blog"]

    def get_blog_titles(self):
        titles = []
        for blog in self.blogs:
            tags = blog.find_all("h3", title="title")
            if len(tags) == 1:
                titles.append(tags[0].contents[0])
            else:
                titles.append(len(tags))
        return titles

    def get_title_and_extra(self, tag):
        couples = []
        for blog in self.blogs:
            titles = blog.find_all(title="title")
            if len(titles) != 1:
                continue
            extras = blog.find_all(title=tag)
            if len(extras) != 1:
                continue
            couples.append((titles[0].contents[0], extras[0].contents[0]))
        return couples


class BlogsTemplateTests(TestCase):
    def setUp(self):
        response = self.client.get("/blog/")
        self.soup = BeautifulSoup(response.content, features="html.parser")

    def test_holds_blog_title(self):
        h1_tags = self.soup.find_all("h1")
        self.assertEqual(len(h1_tags), 1)
        self.assertEqual(h1_tags[0].contents[0], "Blog")

    def test_show_zero_as_the_number_of_blogs(self):
        h2_tags = self.soup.find_all("h2")
        self.assertEqual(len(h2_tags), 1)
        self.assertEqual(h2_tags[0].contents[0], "Xavier has written 0 blogs.")

    def test_no_shown_blog(self):
        extractor = BlogExtractor(self.soup)
        self.assertEqual(len(extractor.blogs), 0)


class BlogsTemplateWithOneBlogTests(TestCase):
    fixtures = ["one_blog.json"]

    def setUp(self):
        response = self.client.get("/blog/")
        self.soup = BeautifulSoup(response.content, features="html.parser")

    def test_show_one_as_the_number_of_blogs(self):
        h2_tags = self.soup.find_all("h2")
        self.assertEqual(len(h2_tags), 1)
        self.assertEqual(h2_tags[0].contents[0], "Xavier has written 1 blogs.")

    def test_show_one_blogs(self):
        extractor = BlogExtractor(self.soup)
        self.assertEqual(len(extractor.blogs), 1)


class BlogsTemplateWithThreeBlogTests(TestCase):
    fixtures = ["three_blogs.json"]

    def setUp(self):
        response = self.client.get("/blog/")
        self.soup = BeautifulSoup(response.content, features="html.parser")
        with open(
            "./blog/fixtures/three_blogs.json", encoding="utf-8"
        ) as json_fixtures:
            fixtures_list = json.load(json_fixtures)

        self.expected_blogs = [
            json_entry["fields"]
            for json_entry in fixtures_list
            if json_entry["model"] == "blog.Blog"
        ]

    def test_show_three_as_the_number_of_blogs(self):
        h2_tags = self.soup.find_all("h2")
        self.assertEqual(len(h2_tags), 1)
        self.assertEqual(h2_tags[0].contents[0], "Xavier has written 3 blogs.")

    def test_show_three_blogs(self):
        extractor = BlogExtractor(self.soup)
        self.assertEqual(len(extractor.blogs), 3)

    def test_titles_are_shown(self):
        extractor = BlogExtractor(self.soup)
        actual_titles = set(extractor.get_blog_titles())

        expected_titles = []
        for blog in self.expected_blogs:
            if isinstance(blog, dict):
                expected_titles.append(blog["title"])
        expected_titles = set(expected_titles)

        self.assertEqual(actual_titles, expected_titles)

    def test_titles_and_texts_are_together_in_blogs(self):
        extractor = BlogExtractor(self.soup)
        actual_title_and_text = set(extractor.get_title_and_extra("text"))

        expected_title_and_text = []
        for blog in self.expected_blogs:
            if isinstance(blog, dict):
                expected_tuple = (blog["title"], blog["text"])
                expected_title_and_text.append(expected_tuple)
        expected_title_and_text = set(expected_title_and_text)

        self.assertEqual(actual_title_and_text, expected_title_and_text)

    def test_titles_and_dates_are_together_in_blogs(self):
        extractor = BlogExtractor(self.soup)
        actual_title_and_date = set(extractor.get_title_and_extra("date"))

        expected_title_and_date = []
        for blog in self.expected_blogs:
            if isinstance(blog, dict) and blog["title"] == "Oldest post":
                expected_title_and_date.append(("Oldest post", "2020 JAN 1"))
            if isinstance(blog, dict) and blog["title"] == "New post":
                expected_title_and_date.append(("New post", "2021 NOV 10"))
            if isinstance(blog, dict) and blog["title"] == "Lorem ipsum":
                expected_title_and_date.append(("Lorem ipsum", "2021 FEB 6"))
        expected_title_and_date = set(expected_title_and_date)

        self.assertEqual(actual_title_and_date, expected_title_and_date)


# to run the tests on command line
# python ./manage.py test blog.tests.test_templates
#
