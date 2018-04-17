import unittest

from selenium import webdriver

from objects.Login import Page


class TC(unittest.TestCase):
    """Test Cura.Login Object"""

    driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_A(self):
        """Test Cura.Login.open() method"""
        Page.open(self.driver)
