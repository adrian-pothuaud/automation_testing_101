from sikuli import *
resetImagePath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "imgs"))


class CURA(object):
    """Page Objects for CURA Application testing"""

    class AppointmentConfirmation(object):
        title = "appointment_confirm_title.png"

    class AppointmentForm(object):
        apply_readmission = Pattern("apply_readmission.png").similar(0.50).targetOffset(-107, -1)
        book = "book.png"
        comment = Pattern("comment.png").targetOffset(125, 7)
        facility = Pattern("facility.png").targetOffset(149, 1)
        facility_values = ["Tokyo CURA Healthcare Center", "Hongkong CURA Healthcare Center",
                           "Seoul CURA Healthcare Center"]
        healtcare_programs = ["medicare.png", "medicaid.png", "none.png"]
        title = "make_appointment_title.png"
        visit_date = Pattern("visit_date.png").targetOffset(168, -4)

    class History(object):
        title = "title.png"
        element = "element.png"

    class Home(object):
        class Menu(object):
            history = "history.png"
            login = "login.png"
            logout = "logout.png"
            toggle = "toggle.png"

        appointment_button = "appointment_button.png"
        title = "CURA_Title.png"
        url = "http://demoaut.katalon.com/"

    class Login(object):
        class Form(object):
            password = "password_field.png"
            submit = "submit.png"
            username = "username_field.png"

        failed = "login_failed.png"
        url = 'http://demoaut.katalon.com/profile.php#login'
