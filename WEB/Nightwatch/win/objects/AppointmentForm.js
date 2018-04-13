module.exports = {

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
        facility : {
            selector : "#combo_facility",
            values : [
                "Tokyo CURA Healthcare Center", 
                "Hongkong CURA Healthcare Center",
                "Seoul CURA Healthcare Center"
            ]
        },
        title : {
            selector : "h2",
            text : "Make Appointment"
        },
        visit_date : {
            selector : "#txt_visit_date"
        }
    },

    sections : {
        healthcare_programs : {
            selector: "#appointment > div > div > form > div:nth-child(3)",
            elements:{
                medicare : {
                    selector : "#radio_program_medicare"
                },
                medicaid : {
                    selector : "#radio_program_medicaid"
                },
                none : {
                    selector : "#radio_program_none"
                }
            }
        }
    },

    url : "http://demoaut.katalon.com/"
}