import random
import sikuli
import string
import unittest
import webbrowser

from CURAObjects import *

DEBUG = True
TIMEOUT = 20

class TC_01(unittest.TestCase):
    """Automated User Story 1"""
    
    @classmethod
    def setUpClass(self):
        self.screen = sikuli.Screen(0)
        self.region = sikuli.Region(self.screen.getBounds())

    def test_A(self):
        """Navigate to CURA Home Page"""
        if DEBUG:
            print("Opening web browser to CURA Home Page")
        webbrowser.open(CURA.Home.url)
        self.region.wait(3)
        self.region.type(Key.UP, Key.WIN)
        self.region.wait(CURA.Home.title, TIMEOUT)
        if DEBUG:
            print("CURA Title image found")
            print(10*"*")

    def test_B(self):
        """Navigate to CURA Login Page"""
        if DEBUG:
            print("Navigation to Login Form")
        self.region.click(CURA.Home.Menu.toggle)
        if DEBUG:
            print("CURA Menu openned")
        self.region.wait(CURA.Home.Menu.login)
        self.region.click(CURA.Home.Menu.login)
        if DEBUG:
            print("Login button clicked")
        self.region.wait(CURA.Login.Form.username, TIMEOUT)
        self.region.wait(CURA.Login.Form.password, TIMEOUT)
        if DEBUG:
            print("CURA Login form found")
            print(10*"*")

    def test_C(self):
        """Fill Login form with valid user"""
        if DEBUG:
            print("Fill Login form with valid user")
        self.region.paste(CURA.Login.Form.username, "John Doe")
        self.region.paste(CURA.Login.Form.password, "ThisIsNotAPassword")
        if DEBUG:
            print("click submit")
        self.region.click(CURA.Login.Form.submit)
        self.region.wait(CURA.AppointmentForm.title, TIMEOUT)
        if DEBUG:
            print("Login success")

    def test_D(self):
        """Create an appointment"""
        if DEBUG:
            print("Appointment creation")
        self.region.click(CURA.AppointmentForm.facility)
        self.region.wait(0.5)
        rnd1 = random.randint(0, 2)
        self.region.type(CURA.AppointmentForm.facility_values[rnd1])
        if DEBUG:
            print("Selected facility: {}".format(CURA.AppointmentForm.facility_values[rnd1]))
        self.region.wait(0.5)
        self.region.Screen(0).getCenter().click()
        self.region.wait(0.5)
        if bool(random.getrandbits(1)):
            self.region.click(CURA.AppointmentForm.apply_readmission)
            if DEBUG:
                print("select readmission option")
        rnd2 = random.randint(0, 2)
        self.region.click(CURA.AppointmentForm.healtcare_programs[rnd2])
        if DEBUG:
            print("Selected healthcare program: {}".format(CURA.AppointmentForm.healtcare_programs[rnd2]))
        year = random.randint(1950, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        self.region.paste(CURA.AppointmentForm.visit_date, ("{}/{}/{}".format(day, month, year)))
        if DEBUG:
            print("Selected visit date: {}".format("{}/{}/{}".format(day, month, year)))
        self.region.paste(CURA.AppointmentForm.comment, "".join([random.choice(string.letters) for i in xrange(15)]))
        if DEBUG:
            print("Filled comments")
        self.region.click(CURA.AppointmentForm.book)
        if DEBUG:
            print("click submit")
        self.region.wait(CURA.AppointmentConfirmation.title, TIMEOUT)
        if DEBUG:
            print("Appointment creation OK")

    def test_E(self):
        """Navigate to History page"""
        if DEBUG:
            print("Going to History page")
        self.region.click(CURA.Home.Menu.toggle)
        self.region.wait(CURA.Home.Menu.history)
        self.region.click(CURA.Home.Menu.history)
        self.region.wait(CURA.History.title, TIMEOUT)
        if DEBUG:
            print("history page opened")

    def test_F(self):
        """Verify 1 element is present"""
        self.assertEqual(len(list(self.region.findAll(CURA.History.element))), 1)
        if DEBUG:
            print("Number of element is 1 (OK)")

    def test_G(self):
        """Logout"""
        if DEBUG:
            print("Logout")
        self.region.click(CURA.Home.Menu.toggle)
        self.region.wait(CURA.Home.Menu.logout)
        self.region.click(CURA.Home.Menu.logout)
        self.region.wait(CURA.Home.title, TIMEOUT)
        if DEBUG:
            print("logout success")
        self.region.type(Key.F4, Key.CTRL)
        wait(1)

class TC_02(unittest.TestCase):
    """Automated User Story 2"""

    @classmethod
    def setUpClass(self):
        self.screen = sikuli.Screen(0)
        self.region = sikuli.Region(self.screen.getBounds())

    def test_A(self):
        """Navigate to CURA Home Page"""
        if DEBUG:
            print("Opening web browser to CURA Home Page")
        webbrowser.open(CURA.Home.url)
        self.region.wait(3)
        self.region.type(Key.UP, Key.WIN)
        self.region.wait(CURA.Home.title, TIMEOUT)
        if DEBUG:
            print("CURA Title image found")
            print(10*"*")

    def test_B(self):
        """Navigate to CURA Login Page"""
        if DEBUG:
            print("Navigation to Login Form")
        self.region.click(CURA.Home.Menu.toggle)
        if DEBUG:
            print("CURA Menu openned")
        self.region.wait(CURA.Home.Menu.login)
        self.region.click(CURA.Home.Menu.login)
        if DEBUG:
            print("Login button clicked")
        self.region.wait(CURA.Login.Form.username, TIMEOUT)
        self.region.wait(CURA.Login.Form.password, TIMEOUT)
        if DEBUG:
            print("CURA Login form found")
            print(10*"*")

    def test_C(self):
        """Fill Login form with invalid user"""
        if DEBUG:
            print("Fill Login form with valid user")
        self.region.paste(CURA.Login.Form.username, "Jane Doe")
        self.region.paste(CURA.Login.Form.password, "ThisIsAPassword")
        if DEBUG:
            print("click submit")
        self.region.click(CURA.Login.Form.submit)
        self.region.wait(CURA.Login.failed, TIMEOUT)
        if DEBUG:
            print("Login failure verified")
        self.region.type(Key.F4, Key.CTRL)
        self.region.wait(1)
