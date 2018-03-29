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
        sikuli.wait("seleniumhq.png", 30)
    def test_C(self):
        """Scroll to the bottom of the page."""
        if sikuli.Env.isWindows():
            wheel_dir = sikuli.WHEEL_DOWN
        else:
            wheel_dir = sikuli.WHEEL_UP
        sikuli.wheel(sikuli.Screen(0), wheel_dir, 50)
    def test_D(self):
        """Verify Footer."""
        sikuli.wait("footer.png", 30)