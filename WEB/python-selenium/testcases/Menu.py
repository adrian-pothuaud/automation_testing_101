import unittest

from selenium import webdriver

from objects.Home import Page
from objects.Shared import Menu


class TC(unittest.TestCase):
    """Test Cura.Menu Object"""

    driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    @classmethod
    def setUpClass(cls):
        Page.open(cls.driver)

    def test_A(self):
        """Test Cura.Menu.navigate_to() method for visitors"""
        Menu.navigate_to(self.driver, "login")
