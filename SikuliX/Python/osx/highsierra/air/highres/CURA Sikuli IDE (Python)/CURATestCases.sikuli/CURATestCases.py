from CURAObjects import *
import os
import random
from sikuli import *
import string
import unittest
import webbrowser

DEBUG = True
TIMEOUT = 20

class TC_01(unittest.TestCase):
    """Automated User Story 1"""

    def test_A(self):
        """Navigate to CURA Home Page"""
        if DEBUG: 
            print("Opening web browser to CURA Home Page")
        webbrowser.open(CURA.Home.url)
        wait(3)
        type(Key.UP, Key.WIN)
        wait(CURA.Home.title, TIMEOUT)
        if DEBUG: 
            print("CURA Title image found")
            print(10*"*")

    def test_B(self):
        """Navigate to CURA Login Page"""
        if DEBUG: 
            print("Navigation to Login Form")
        click(CURA.Home.Menu.toggle)
        if DEBUG: 
            print("CURA Menu openned")
        wait(CURA.Home.Menu.login)
        click(CURA.Home.Menu.login)
        if DEBUG: 
            print("Login button clicked")
        wait(CURA.Login.Form.username, TIMEOUT)
        wait(CURA.Login.Form.password, TIMEOUT)
        if DEBUG: 
            print("CURA Login form found")
            print(10*"*")

    def test_C(self):
        """Fill Login form with valid user"""
        if DEBUG: 
            print("Fill Login form with valid user")
        paste(CURA.Login.Form.username, "John Doe")
        paste(CURA.Login.Form.password, "ThisIsNotAPassword")
        if DEBUG: 
            print("click submit")
        click(CURA.Login.Form.submit)
        wait(CURA.AppointmentForm.title, TIMEOUT)
        if DEBUG: 
            print("Login success")

    def test_D(self):
        """Create an appointment"""
        if DEBUG: 
            print("Appointment creation")
        click(CURA.AppointmentForm.facility)
        wait(0.5)
        rnd1 = random.randint(0, 2)
        type(CURA.AppointmentForm.facility_values[rnd1])
        if DEBUG: 
            print("Selected facility: {}".format(CURA.AppointmentForm.facility_values[rnd1]))
        wait(0.5)
        Screen(0).getCenter().click()
        wait(0.5)
        if bool(random.getrandbits(1)):
            click(CURA.AppointmentForm.apply_readmission)
            if DEBUG: 
                print("select readmission option")
        rnd2 = random.randint(0, 2)
        click(CURA.AppointmentForm.healtcare_programs[rnd2])
        if DEBUG: 
            print("Selected healthcare program: {}".format(CURA.AppointmentForm.healtcare_programs[rnd2]))
        year = random.randint(1950, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        paste(CURA.AppointmentForm.visit_date, ("{}/{}/{}".format(day, month, year)))
        if DEBUG: 
            print("Selected visit date: {}".format("{}/{}/{}".format(day, month, year)))
        paste(CURA.AppointmentForm.comment, "".join([random.choice(string.letters) for i in xrange(15)]))
        if DEBUG:
            print("Filled comments")
        click(CURA.AppointmentForm.book)
        if DEBUG:
            print("click submit")
        wait(CURA.AppointmentConfirmation.title, TIMEOUT)
        if DEBUG:
            print("Appointment creation OK")

    def test_E(self):
        """Navigate to History page"""
        if DEBUG:
            print("Going to History page")
        click(CURA.Home.Menu.toggle)
        wait(CURA.Home.Menu.history)
        click(CURA.Home.Menu.history)
        wait(CURA.History.title, TIMEOUT)
        if DEBUG:
            print("history page opened")

    def test_F(self):
        """Verify 1 element is present"""
        self.assertEqual(len(list(findAll(CURA.History.element))), 1)
        if DEBUG:
            print("Number of element is 1 (OK)")

    def test_G(self):
        """Logout"""
        if DEBUG:
            print("Logout")
        click(CURA.Home.Menu.toggle)
        wait(CURA.Home.Menu.logout)
        click(CURA.Home.Menu.logout)
        wait(CURA.Home.title, TIMEOUT)
        if DEBUG:
            print("logout success")
        type(Key.F4, Key.CTRL)
        wait(1)

class TC_02(unittest.TestCase):
    """Automated User Story 2"""

    def test_A(self):
        """Navigate to CURA Home Page"""
        if DEBUG: 
            print("Opening web browser to CURA Home Page")
        webbrowser.open(CURA.Home.url)
        wait(3)
        type(Key.UP, Key.WIN)
        wait(CURA.Home.title, TIMEOUT)
        if DEBUG: 
            print("CURA Title image found")
            print(10*"*")

    def test_B(self):
        """Navigate to CURA Login Page"""
        if DEBUG: 
            print("Navigation to Login Form")
        click(CURA.Home.Menu.toggle)
        if DEBUG: 
            print("CURA Menu openned")
        wait(CURA.Home.Menu.login)
        click(CURA.Home.Menu.login)
        if DEBUG: 
            print("Login button clicked")
        wait(CURA.Login.Form.username, TIMEOUT)
        wait(CURA.Login.Form.password, TIMEOUT)
        if DEBUG: 
            print("CURA Login form found")
            print(10*"*")

    def test_C(self):
        """Fill Login form with invalid user"""
        if DEBUG: 
            print("Fill Login form with valid user")
        paste(CURA.Login.Form.username, "Jane Doe")
        paste(CURA.Login.Form.password, "ThisIsAPassword")
        if DEBUG: 
            print("click submit")
        click(CURA.Login.Form.submit)
        wait(CURA.Login.failed, TIMEOUT)
        if DEBUG: 
            print("Login failure verified")
        type(Key.F4, Key.CTRL)
        wait(1)

if __name__ == "__main__":

    click(CURA.AppointmentForm.facility)
    wait(0.5)
    rnd1 = random.randint(0, 2)
    type(CURA.AppointmentForm.facility_values[rnd1])
    if DEBUG: 
        print("Selected facility: {}".format(CURA.AppointmentForm.facility_values[rnd1]))
    wait(0.5)
    Screen(0).getCenter().click()
    wait(0.5)
    if bool(random.getrandbits(1)):
        click(CURA.AppointmentForm.apply_readmission)
        if DEBUG: 
            print("select readmission option")