from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os


class HomeTemplateTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(HomeTemplateTests, cls).setUpClass()
        options = Options()
        options.headless = True
        if os.name == "nt":
            driver_exe = "utils/geckodriver.exe"
        cls.driver = webdriver.Firefox(
            options=options, executable_path=driver_exe, service_log_path=os.devnull
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        super(HomeTemplateTests, cls).tearDownClass()

    def test_expected_failure(self):
        self.driver.get("%s%s" % (self.live_server_url, ""))
        elements = self.driver.find_elements(By.TAG_NAME, "h1")
        self.assertEqual(2, len(elements))
