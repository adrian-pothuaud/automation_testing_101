package cura.objects;

import org.sikuli.script.Pattern;

public class Home {

    public static class Menu {

        public static Pattern history = new Pattern("imgs/history.png");
        public static Pattern login = new Pattern("imgs/login.png");
        public static Pattern logout = new Pattern("imgs/logout.png");
        public static Pattern toggle = new Pattern("imgs/toggle.png");
    }

    public static Pattern appointment_button = new Pattern("imgs/appointment_button.png");
    public static Pattern title = new Pattern("imgs/CURA_title.png");
    public static String url = "http://demoaut.katalon.com/";
}
