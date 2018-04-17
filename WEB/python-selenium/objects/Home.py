from selenium.webdriver.support import ui


class Page:
    def __init__(self):
        pass

    class appointment_button:
        def __init__(self):
            pass

        selector = "#btn-make-appointment"

    class title:
        def __init__(self):
            pass

        selector = "h1"
        text = "CURA Healthcare Service"

    url = "http://demoaut.katalon.com/"

    # noinspection PyShadowingNames
    @classmethod
    def open(cls, driver):
        wait = ui.WebDriverWait(driver, 30)
        driver.get(cls.url)
        wait.until(lambda driver: driver.find_element_by_css_selector(cls.title.selector))
