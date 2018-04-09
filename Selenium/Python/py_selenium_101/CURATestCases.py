from CURAObjects import *
import random
from selenium import webdriver
import string
import unittest

DEBUG = True
TIMEOUT = 20

class TC_01(unittest.TestCase):
    """Automated User Story 1"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(self):
        self.driver.close()

    def test_A(self):
        """Navigate to CURA Home Page"""
        self.driver.get(CURA.Home.url)

    def test_B(self):
        """Navigate to CURA Login Page"""
        self.driver.find_element_by_css_selector(
            CURA.Home.Menu.toggle.css
        ).click()
        self.driver.find_element_by_css_selector(
            CURA.Home.Menu.login.css
        ).click()

    def test_C(self):
        """Fill Login form with valid user"""
        self.driver.find_element_by_css_selector(
            CURA.Login.Form.username.css
        ).send_keys("John Doe")
        self.driver.find_element_by_css_selector(
            CURA.Login.Form.password.css
        ).send_keys("ThisIsNotAPassword")
        self.driver.find_element_by_css_selector(
            CURA.Login.Form.submit.css
        ).click()

    def test_D(self):
        """Create an appointment"""
        # pick random to choose facility
        rdm1 = random.randint(0, 2)
        self.driver.find_element_by_css_selector(
            CURA.AppointmentForm.facility.css
        ).send_keys(
            CURA.AppointmentForm.facility.values[rdm1]
        )
        # pick random for apply readmission option
        rdm2 = bool(random.getrandbits(1))
        if rdm2:
            self.driver.find_element_by_css_selector(
                CURA.AppointmentForm.apply_readmission.css
            ).click()
        # pick random for healthcare program
        rdm3 = random.randint(0, 2)
        if rdm3 == 0:
            self.driver.find_element_by_css_selector(
                CURA.AppointmentForm.healtcare_programs.medicaid.css
            ).click()
        elif rdm3 == 1:
            self.driver.find_element_by_css_selector(
                CURA.AppointmentForm.healtcare_programs.medicare.css
            ).click()
        else:
            self.driver.find_element_by_css_selector(
                CURA.AppointmentForm.healtcare_programs.none.css
            ).click()
        # type visit date
        rdm_year = random.randint(2019, 2030)
        rdm_month = random.randint(1, 12)
        rdm_day = random.randint(1, 31)
        self.driver.find_element_by_css_selector(
            CURA.AppointmentForm.visit_date.css
        ).send_keys(
            "{}/{}/{}".format(rdm_day, rdm_month, rdm_year)
        )
        # insert comment
        self.driver.find_element_by_css_selector(
            CURA.AppointmentForm.comment.css
        ).send_keys(
            "### Automatic Tests input"
        )
        # validate
        self.driver.find_element_by_css_selector(
            CURA.AppointmentForm.book.css
        ).click()

    def test_E(self):
        """Navigate to History page"""
        self.driver.find_element_by_css_selector(
            CURA.Home.Menu.toggle.css
        ).click()
        self.driver.find_element_by_css_selector(
            CURA.Home.Menu.history.css
        ).click()

    def test_F(self):
        """Verify 1 element is present"""
        self.driver.find_element_by_css_selector(CURA.AppointmentConfirmation.title.css).

    def test_G(self):
        """Logout"""
        self.driver.find_element_by_css_selector(
            CURA.Home.Menu.toggle.css
        ).click()
        self.driver.find_element_by_css_selector(
            CURA.Home.Menu.logout.css
        ).click()

class TC_02(unittest.TestCase):
    """Automated User Story 2"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(self):
        self.driver.close()

    def test_A(self):
        """Navigate to CURA Home Page"""
        self.driver.get(CURA.Home.url)

    def test_B(self):
        """Navigate to CURA Login Page"""
        self.driver.find_element_by_css_selector(CURA.Home.Menu.toggle.css).click()
        self.driver.find_element_by_css_selector(CURA.Home.Menu.login.css).click()

    def test_C(self):
        """Fill Login form with invalid user"""
        self.driver.find_element_by_css_selector(CURA.Login.Form.username.css).send_keys("Jane Doe")
        self.driver.find_element_by_css_selector(CURA.Login.Form.password.css).send_keys("ThisIsAPassword")
        self.driver.find_element_by_css_selector(CURA.Login.Form.submit.css).click()

