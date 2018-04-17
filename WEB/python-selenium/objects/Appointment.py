from selenium.webdriver.support import ui


class ConfirmationPage:
    """Page after appointent creation success"""

    def __init__(self):
        pass

    url = "http://demoaut.katalon.com/appointment.php#summary"

    class title:
        def __init__(self):
            pass

        selector = "h1"
        text = "CURA Healthcare Service"

    # noinspection PyShadowingNames
    @classmethod
    def open(cls, driver):
        wait = ui.WebDriverWait(driver, 30)
        driver.get(cls.url)
        wait.until(lambda driver: driver.find_element_by_css_selector(cls.title.selector))


class Form:
    def __init__(self):
        pass

    class apply_readmission:
        def __init__(self):
            pass

        selector = "#chk_hospotal_readmission"

    class book:
        def __init__(self):
            pass

        selector = "#btn-book-appointment"

    class comment:
        def __init__(self):
            pass

        selector = "#txt_comment"

    class facility:
        def __init__(self):
            pass

        selector = "#combo_facility"
        values = [
            "Tokyo CURA Healthcare Center",
            "Hongkong CURA Healthcare Center",
            "Seoul CURA Healthcare Center"
        ]

    class healtcare_programs:
        def __init__(self):
            pass

        class medicare:
            def __init__(self):
                pass

            selector = "#radio_program_medicare"

        class medicaid:
            def __init__(self):
                pass

            selector = "#radio_program_medicaid"

        class none:
            def __init__(self):
                pass

            selector = "#radio_program_none"

    class title:
        def __init__(self):
            pass

        selector = "h2"
        text = "Make Appointment"

    class visit_date:
        def __init__(self):
            pass

        selector = "#txt_visit_date"

    url = "http://demoaut.katalon.com/"

    # noinspection PyShadowingNames
    @classmethod
    def open(cls, driver):
        wait = ui.WebDriverWait(driver, 30)
        driver.get(cls.url)
        wait.until(lambda driver: driver.find_element_by_css_selector(cls.title.selector))

    @classmethod
    def fill(cls, driver, facility_value, apply_readmission, healthcare_program, visit_date, comment):
        driver.find_element_by_css_selector(
            cls.facility.selector
        ).send_keys(
            facility_value
        )
        # pick random for apply readmission option
        if apply_readmission:
            driver.find_element_by_css_selector(
                cls.apply_readmission.selector
            ).click()
        # select healthcare program
        driver.find_element_by_css_selector(
            healthcare_program.selector
        ).click()
        # type visit date
        driver.find_element_by_css_selector(
            cls.visit_date.selector
        ).send_keys(
            visit_date
        )
        # insert comment
        driver.find_element_by_css_selector(
            cls.comment.selector
        ).send_keys(
            comment
        )
        # submit
        driver.find_element_by_css_selector(
            cls.book.selector
        ).click()
