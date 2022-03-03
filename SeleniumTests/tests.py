from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


class FirstSeleniumTest(LiveServerTestCase):

    def setUp(self):
        service = Service(executable_path=GeckoDriverManager().install())
        self.browser = webdriver.Firefox(service=service)

    def tearDown(self):
        self.browser.quit()

    def test_check_homepage(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Home', self.browser.title)
