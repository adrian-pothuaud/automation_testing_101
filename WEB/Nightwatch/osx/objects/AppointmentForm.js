module.exports = {

    commands : {

        create_appointment : function(apply, comment, facility, healtcare_program, visit_date) {
            console.log("Appointment Creation ...");
            // ToDo
        }
    },

    elements : {

        apply_readmission : {
            selector : "#chk_hospotal_readmission"
        },
        book : {
            selector : "#btn-book-appointment"
        },
        comment : {
            selector : "#txt_comment"
        },
        facillity : {
            selector : "#combo_facility",
            values : [
                "Tokyo CURA Healthcare Center", 
                "Hongkong CURA Healthcare Center",
                "Seoul CURA Healthcare Center"
            ]
        },
        healthcare_programs : {
            medicare : {
                selector : "#radio_program_medicare"
            },
            medicaid : {
                selector : "#radio_program_medicaid"
            },
            none : {
                selector : "#radio_program_none"
            }
        },
        title : {
            selector : "h2",
            text : "Make Appointment"
        },
        visit_date : {
            selector : "#txt_visit_date"
        }
    },

    url : "http://demoaut.katalon.com/"
}