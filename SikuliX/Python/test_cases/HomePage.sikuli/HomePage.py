import httplib
import unittest

class TC(unittest.TestCase):
    """Test Case for Home Page."""

    def test_A(self):
        """Make an HTTP request then verify Response code."""
        conn = httplib.HTTPConnection("www.seleniumhq.org")
        conn.request("HEAD", "/")
        self.assertEquals(conn.getresponse().status, 200)