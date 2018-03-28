import sikuli
import unittest
import webbrowser

class TC(unittest.TestCase):
    """Test Case for Home Page."""

    def test_A(self):
        """Open Home Page and wait for Selenium Image."""
        webbrowser.open("http://www.seleniumhq.org")
        sikuli.wait("1522273020361.png", 30)