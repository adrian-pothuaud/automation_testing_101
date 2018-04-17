package cura;

import java.util.Date;

public class Appointment {

    private String facility;
    private Boolean readmission;
    private String healthcare_program;
    private String visit_date;
    private String comment;

    public Appointment(String facility, Boolean readmission, String healthcare_program, String visit_date, String comment) {
        this.facility = facility;
        this.readmission = readmission;
        this.healthcare_program = healthcare_program;
        this.visit_date = visit_date;
        this.comment = comment;
    }

    public String getFacility() {
        return facility;
    }

    public void setFacility(String facility) {
        this.facility = facility;
    }

    public Boolean getReadmission() {
        return readmission;
    }

    public void setReadmission(Boolean readmission) {
        this.readmission = readmission;
    }

    public String getHealthcare_program() {
        return healthcare_program;
    }

    public void setHealthcare_program(String healthcare_program) {
        this.healthcare_program = healthcare_program;
    }

    public String getVisit_date() {
        return visit_date;
    }

    public void setVisit_date(String visit_date) {
        this.visit_date = visit_date;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    @Override
    public String toString() {
        return "Appointment{" +
                "facility='" + facility + '\'' +
                ", readmission=" + readmission +
                ", healthcare_program='" + healthcare_program + '\'' +
                ", visit_date='" + visit_date + '\'' +
                ", comment='" + comment + '\'' +
                '}';
    }
}
