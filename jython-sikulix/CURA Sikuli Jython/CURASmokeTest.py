import HtmlTestRunner
import os
import unittest

import CURATestCases

test_suite = unittest.TestSuite()
test_loader = unittest.TestLoader()

test_list = [CURATestCases.TC_01, CURATestCases.TC_02 ]
for test in test_list:
    tests = test_loader.loadTestsFromTestCase(test)
    test_suite.addTests(tests)

test_runner = HtmlTestRunner.HTMLTestRunner(
    output=os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports"),
    descriptions="CURA SmokeTests (AUTOMATED)",
    report_title="CURA SmokeTest"
)

test_runner.run(test_suite)
