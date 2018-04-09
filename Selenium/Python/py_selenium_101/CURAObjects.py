class CURA:
    """Page Objects for CURA Application testing"""

    class AppointmentConfirmation:

        class title:

            css = "h1"
            text = "CURA Healthcare Service"

        url = "http://demoaut.katalon.com/appointment.php#summary"

    class AppointmentForm:

        class apply_readmission:

            css = "#chk_hospotal_readmission"

        class book:

            css = "#btn-book-appointment"

        class comment:

            css = "#txt_comment"

        class facility:

            css = "#combo_facility"
            values = [
                "Tokyo CURA Healthcare Center", 
                "Hongkong CURA Healthcare Center",
                "Seoul CURA Healthcare Center"
            ]
            
        class healtcare_programs:
            
            class medicare:
                
                css = "#radio_program_medicare"

            class medicaid:

                css = "#radio_program_medicaid"

            class none:

                css = "#radio_program_none"

        class title:

            css = "h2"
            text = "Make Appointment"

        class visit_date:

            css = "#txt_visit_date"

        url = "http://demoaut.katalon.com/"

    class History:

        class title:

            css = "h2"
            text = "History"

        class element:

            css = ".panel-info"

        url = "http://demoaut.katalon.com/history.php#history"

    class Home:

        class Menu:

            class history:

                css = "ul.sidebar-nav > li:nth-of-type(3) > a"

            class login:

                css = "ul.sidebar-nav > li:nth-of-type(3) > a"

            class logout:

                css = "ul.sidebar-nav > li:nth-of-type(5) > a"

            class toggle:

                css = "#menu-toggle"

        class appointment_button:

                css = "#btn-make-appointment"

        class title:

            css = "h1"
            text = "CURA Healthcare Service"

        url = "http://demoaut.katalon.com/"

    class Login:

        class Form:

            class password:

                css = "#txt-password"

            class submit:

                css = "#btn-login"

            class username:

                css = "#txt-username"

            class failed:

                css = "p.lead.text-danger"
                text = "Login failed! Please ensure the username and password are valid."

        url = "http://demoaut.katalon.com/profile.php#login"