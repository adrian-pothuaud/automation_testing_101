package cura;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import java.util.Arrays;
import java.util.List;

public class Home {
    public static By createAppointmentBtn = new By.ById("btn-make-appointment");
    public static class AppointmentForm {
        static By facility_select = new By.ByCssSelector("#combo_facility");
        static List<String> facility_values = Arrays.asList(
                "Tokyo CURA Healthcare Center",
                "Hongkong CURA Healthcare Center",
                "Seoul CURA Healthcare Center"
        );
        static By apply_readmission = new By.ById("chk_hospotal_readmission");
        static List<By.ById> healthcare_programs = Arrays.asList(
                new By.ById("radio_program_medicare"),
                new By.ById("radio_program_medicaid"),
                new By.ById("radio_program_none")
        );
        static By visit_date = new By.ById("txt_visit_date");
        static By comment = new By.ById("txt_comment");
        static By submit = new By.ById("btn-book-appointment");
    }
    private static void createAppointment(WebDriver driver, int facility_nb, Boolean apply_readmission, int healthcare_program_nb, String visit_date, String comment) {
        driver.findElement(AppointmentForm.facility_select).sendKeys(AppointmentForm.facility_values.get(facility_nb));
        if (apply_readmission) {
            driver.findElement(AppointmentForm.apply_readmission).click();
        }
        driver.findElement(AppointmentForm.healthcare_programs.get(healthcare_program_nb)).click();
        driver.findElement(AppointmentForm.visit_date).sendKeys(visit_date);
        driver.findElement(AppointmentForm.comment).sendKeys(comment);
        driver.findElement(AppointmentForm.submit).click();
    }
    public static void createAppointment(WebDriver driver, Appointment appointment) {
        int facility_nb = AppointmentForm.facility_values.indexOf(appointment.getFacility());
        int healthcare_nb;
        if (appointment.getHealthcare_program().toLowerCase().equals("medicaid")) {
            healthcare_nb = 0;
        } else if (appointment.getHealthcare_program().toLowerCase().equals("medicare")) {
            healthcare_nb = 1;
        } else {
            healthcare_nb = 2;
        }
        createAppointment(
                driver,
                facility_nb,
                appointment.getReadmission(),
                healthcare_nb,
                appointment.getVisit_date(),
                appointment.getComment()
        );
    }

    public static class AppointmentConfirm {
        public static By summary = new By.ById("summary");
    }
}
