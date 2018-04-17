import unittest

from selenium import webdriver

from objects.Appointment import Form as AppointmentForm
from objects.Login import Page as Login


class Form(unittest.TestCase):
    """Test AppointmentConfirm Object"""

    driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    @classmethod
    def setUpClass(cls):
        Login.open(cls.driver)
        Login.fill(cls.driver, "John Doe", "ThisIsNotAPassword")

    def test_A(self):
        """Create an Appointment"""
        AppointmentForm.fill(
            self.driver,
            AppointmentForm.facility.values[1],
            True,
            AppointmentForm.healtcare_programs.medicaid,
            "23-05-2020",
            "Unit tests"
        )

    pass
