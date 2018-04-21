import unittest
from selenium import webdriver
from resource.url_site import PathUrl
from resource.path_driver import GetDriver
from caesar_items.pages.login_page import LogInPage
import logging


class TestBase(unittest.TestCase):
    def setUp(self):
        """ Open Chrome browser."""
        self.driver = webdriver.Chrome(
            executable_path=GetDriver.CHROME_DRIVER)
        self.driver.get(PathUrl.SITE_URL)
        self.driver.maximize_window()
        self.login_page = LogInPage(self.driver)
        logging.basicConfig(filename="test.log", level=logging.WARNING,
                            format='%(levelname)s:%(name)s:[%(funcName)s]:%(message)s')
        logging.warning('\nTest is running!...')

    def tearDown(self):
        logging.warning('\nTest was finished!\n')
        self.driver.quit()
