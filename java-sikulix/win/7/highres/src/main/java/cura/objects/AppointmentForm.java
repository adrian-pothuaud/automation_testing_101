package cura.objects;

import org.sikuli.script.Pattern;

import java.util.ArrayList;
import java.util.List;

public class AppointmentForm {

    public static Pattern apply_readmission = new Pattern("imgs/apply_readmission.png").targetOffset(-107,-1);
    public static Pattern book = new Pattern("imgs/book.png");
    public static Pattern comment = new Pattern("imgs/comment.png").targetOffset(125,7);
    public static Pattern facility = new Pattern("imgs/facility.png").targetOffset(149,1);
    public static List<String> facility_values = new ArrayList<String>(){{
        add("Tokyo CURA Healthcare Center");
        add("Hongkong CURA Healthcare Center");
        add("Seoul CURA Healthcare Center");
    }};
    public static List<Pattern> healthcare_programs = new ArrayList<Pattern>(){{
        add(new Pattern("imgs/medicare.png"));
        add(new Pattern("imgs/medicaid.png"));
        add(new Pattern("imgs/none.png"));
    }};
    public static Pattern title = new Pattern("imgs/make_appointment_title.png");
    public static Pattern visit_date = new Pattern("imgs/visit_date.png").targetOffset(168,-4);
}
