import datetime
import os
import unittest

from testcases.Appointment import Form
from testcases.Home import TC as HomeTC
from testcases.Login import TC as LoginTC
from testcases.Menu import TC as MenuTC
from utils import HTMLTestRunner

test_suite = unittest.TestSuite()
test_loader = unittest.TestLoader()

test_list = [
    Form,
    HomeTC,
    LoginTC,
    MenuTC
]
for test in test_list:
    tests = test_loader.loadTestsFromTestCase(test)
    test_suite.addTests(tests)

now = datetime.datetime.now()

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "reports",
    "unit_tests",
    "TestReport_CURAPageObjects_{}_{}_{}_{}h{}.html".format(
        now.day,
        now.month,
        now.year,
        now.hour,
        now.minute
    )
), "w") as fp:
    test_runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        verbosity=1,
        title="CURA Test Suite",
        description="Automated Tests for CURA PageObjects"
    )

    test_runner.run(test_suite)
