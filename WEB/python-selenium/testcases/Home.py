import unittest

from selenium import webdriver

from objects.Home import Page


class TC(unittest.TestCase):
    """Test Cura.Home Object"""

    driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_A(self):
        """Test Cura.Home.open() method"""
        Page.open(self.driver)
