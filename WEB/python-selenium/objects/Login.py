from selenium.webdriver.support import ui


class Page:

    def __init__(self):
        pass

    class password:
        def __init__(self):
            pass

        selector = "#txt-password"

    class submit:
        def __init__(self):
            pass

        selector = "#btn-login"

    class username:
        def __init__(self):
            pass

        selector = "#txt-username"

    class title:
        def __init__(self):
            pass

        selector = "h1"

    class failed:
        def __init__(self):
            pass

        selector = "p.lead.text-danger"
        text = "Login failed! Please ensure the username and password are valid."

    url = "http://demoaut.katalon.com/profile.php#login"

    @classmethod
    def fill(cls, driver, username, password):
        driver.find_element_by_css_selector(
            cls.username.selector
        ).send_keys(username)
        driver.find_element_by_css_selector(
            cls.password.selector
        ).send_keys(password)
        driver.find_element_by_css_selector(
            cls.submit.selector
        ).click()

    # noinspection PyShadowingNames
    @classmethod
    def open(cls, driver):
        wait = ui.WebDriverWait(driver, 30)
        driver.get(cls.url)
        wait.until(lambda driver: driver.find_element_by_css_selector(cls.title.selector))
