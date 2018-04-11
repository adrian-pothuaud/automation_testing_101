import CURATestCases
import HtmlTestRunner
import os
import unittest

test_suite = unittest.TestSuite()
test_loader = unittest.TestLoader()

test_list = [CURATestCases.TC_01, CURATestCases.TC_02]
for test in test_list:
    tests = test_loader.loadTestsFromTestCase(test)
    test_suite.addTests(tests)

test_report_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report")

test_runner = HtmlTestRunner.HTMLTestRunner(output=test_report_folder)

test_runner.run(test_suite)
