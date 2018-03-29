import datetime
import HTMLTestRunner
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(getBundlePath()), "test_cases"))

import HomePage

test_loadr = unittest.TestLoader()
test_suite = unittest.TestSuite()
test_cases = [
    HomePage.TC,
]
for test_case in test_cases:
    test_suite.addTests(test_loadr.loadTestsFromTestCase(test_case))
with open(os.path.join(os.path.dirname(getBundlePath()), "reports", "testSuite{}.html".format(datetime.datetime.now())), "w") as stream:
    test_runner = HTMLTestRunner.HTMLTestRunner(stream)
    test_runner.run(test_suite)