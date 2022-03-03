import selenium.common.exceptions
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


class FirstSeleniumTest(LiveServerTestCase):

    def setUp(self):
        service = Service(executable_path=GeckoDriverManager().install())
        self.browser = webdriver.Firefox(service=service)

    def tearDown(self):
        pass
        #self.browser.quit()

    def test_check_homepage_opens(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Home', self.browser.title)

    def test_create_user(self):
        #print('test_create_user: registration URL:\t' + self.live_server_url+'register')
    #goto create account page
        registration_URL  = self.live_server_url+'/register'
        self.browser.get(registration_URL)
    #verify middleware token is on page
        self.assertFalse(self.browser.find_element(By.NAME, 'csrfmiddlewaretoken').is_displayed())
    #enter email
        email_input_id = 'id_email'
        test_email = 'fake_email@fake.email'
        email_input = self.browser.find_element(By.ID, email_input_id)
        email_input.send_keys(test_email)
        time.sleep(1.5)
    #enter name
        name_input_id = 'id_name'
        test_name = 'Dubious Fakename'
        name_input = self.browser.find_element(By.ID, name_input_id)
        name_input.send_keys(test_name)
        time.sleep(1.5)
    #enter password
        password_input_id = 'id_password1'
        confirm_password_input_id = 'id_password2'
        test_password = 'one2three59two77'
        password_input = self.browser.find_element(By.ID, password_input_id)
        password_input.send_keys(test_password)
        confirm_password_input = self.browser.find_element(By.ID, confirm_password_input_id)
        confirm_password_input.send_keys(test_password)
        time.sleep(1.5)
    #submit form
        confirm_password_input.submit()

    #verify we are on homepage and logged into new account
        time.sleep(3)
        print(self.browser.title)
        self.assertIn('Home', self.browser.title)
        try:
            self.browser.find_element(By.PARTIAL_LINK_TEXT, test_email)
        except selenium.common.exceptions.NoSuchElementException:
            self.fail("Unable to locate element by partial link: " + test_email)


