module.exports = {

    commands : {

        create_appointment : function(apply, comment, facility, healtcare_program, visit_date) {
            console.log("Appointment Creation ...");
            // ToDo
        }
    },

    elements : {

        apply_readmission : "#chk_hospotal_readmission",
        book : "#btn-book-appointment",
        comment : "#txt_comment",
        facillity : {
            selector : "#combo_facility",
            values : [
                "Tokyo CURA Healthcare Center", 
                "Hongkong CURA Healthcare Center",
                "Seoul CURA Healthcare Center"
            ]
        },
        healthcare_programs : {
            medicare : "#radio_program_medicare",
            medicaid : "#radio_program_medicaid",
            none : "#radio_program_none"
        },
        title : {
            selector : "h2",
            text : "Make Appointment"
        },
        visit_date : "#txt_visit_date"
    },

    url : "http://demoaut.katalon.com/"
}