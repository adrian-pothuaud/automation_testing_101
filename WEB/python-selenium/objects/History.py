from selenium.webdriver.support import ui


class Page:
    def __init__(self):
        pass

    class title:
        def __init__(self):
            pass

        selector = "h2"
        text = "History"

    class element:
        def __init__(self):
            pass

        selector = ".panel-info"

    url = "http://demoaut.katalon.com/history.php#history"

    # noinspection PyShadowingNames
    @classmethod
    def open(cls, driver):
        wait = ui.WebDriverWait(driver, 30)
        driver.get(cls.url)
        wait.until(lambda driver: driver.find_element_by_css_selector(cls.title.selector))

    @classmethod
    def count_elements(cls, driver):
        pass
