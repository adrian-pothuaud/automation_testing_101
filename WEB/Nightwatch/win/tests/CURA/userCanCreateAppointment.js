module.exports = {
    'CURA Test : User Can Login' : function (client) {
        var myLoginPage = client.page.Login();
        var myHomePage = client.page.Home();
        var myAppointmentFormPage = client.page.AppointmentForm();
        var healthcare_programs = myAppointmentFormPage.section.healthcare_programs;
        var myAppointmentConfirmPage = client.page.AppointmentConfirm();

        myLoginPage
            .navigate()
            .waitForElementVisible('@username', 1000)
            .setValue('@username', 'John Doe')
            .setValue('@password', 'ThisIsNotAPassword')
            .click('@submit');

        myHomePage
            .waitForElementVisible('@appointment_button', 3000)
            .click('@appointment_button');

        myAppointmentFormPage
            .waitForElementVisible('@title', 3000)
            .setValue('@facility', "Hongkong CURA Healthcare Center")
            .click('@apply_readmission');

        healthcare_programs
            .click('@medicare');

        myAppointmentFormPage
            .setValue('@visit_date', '05-05-2015')
            .setValue('@comment', 'Automatic test comment')
            .click('@book');

        myAppointmentConfirmPage
            .waitForElementVisible('@title', 3000);
        
        client.end();
    }
  };