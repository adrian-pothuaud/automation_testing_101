import CURATestCases
import HTMLTestRunner
import os
from sikuli import *
import unittest

test_suite = unittest.TestSuite()
test_loader = unittest.TestLoader()

test_list = [CURATestCases.TC_01, CURATestCases.TC_02]
for test in test_list:
    tests = test_loader.loadTestsFromTestCase(test)
    test_suite.addTests(tests)

test_report_file = os.path.join(os.path.dirname(getBundlePath()), "report", "latest.html")
test_report_stream = open(test_report_file, "w")

test_runner = HTMLTestRunner.HTMLTestRunner(stream=test_report_stream, 
    title="CURA Healtcare Service - Automated Tests Suite", 
    description="Sanity tests for CURA Healthcare Service Web Application.",
    dirTestScreenshots=os.path.join(os.path.dirname(getBundlePath()), "report", "screenshots")
)

test_runner.run(test_suite)

test_report_stream.close()