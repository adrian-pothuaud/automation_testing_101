import sikuli
import unittest
import webbrowser

class TC(unittest.TestCase):
    """Test Case for Home Page."""

    def test_A(self):
        """Open SeleniumHQ Home Page."""
        webbrowser.open("http://www.seleniumhq.org")
    def test_B(self):
        """Wait for SeleniumHQ image."""
        sikuli.wait("1522273020361.png", 30)
    def test_C(self):
        """Scroll to the bottom of the page."""
        if sikuli.Env.isWindows():
            sikuli.wheel(sikuli.Screen(0), sikuli.WHEEL_DOWN, 50)
        else:
            sikuli.wheel(sikuli.Screen(0), sikuli.WHEEL_UP, 50)
    def test_D(self):
        """Verify Footer."""
        sikuli.wait("1522293751817.png", 30)