class Menu:
    def __init__(self):
        pass

    class history:
        def __init__(self):
            pass

        selector = "ul.sidebar-nav > li:nth-of-type(3) > a"

    class login:
        def __init__(self):
            pass

        selector = "ul.sidebar-nav > li:nth-of-type(3) > a"

    class logout:
        def __init__(self):
            pass

        selector = "ul.sidebar-nav > li:nth-of-type(5) > a"

    class profile:
        def __init__(self):
            pass

        selector = "ul.sidebar-nav > li:nth-of-type(4) > a"

    class toggle:
        def __init__(self):
            pass

        selector = "#menu-toggle"

    @classmethod
    def navigate_to(cls, driver, param):
        if param == "login":
            driver.find_element_by_css_selector(
                cls.toggle.selector
            ).click()
            driver.find_element_by_css_selector(
                cls.login.selector
            ).click()
        elif param == "history":
            driver.find_element_by_css_selector(
                cls.toggle.selector
            ).click()
            driver.find_element_by_css_selector(
                cls.history.selector
            ).click()
        elif param == "logout":
            driver.find_element_by_css_selector(
                cls.toggle.selector
            ).click()
            driver.find_element_by_css_selector(
                cls.logout.selector
            ).click()
        elif param == "profile":
            driver.find_element_by_css_selector(
                cls.toggle.selector
            ).click()
            driver.find_element_by_css_selector(
                cls.profile.selector
            ).click()
        else:
            raise Exception("Param: {} is not supported".format(param))
