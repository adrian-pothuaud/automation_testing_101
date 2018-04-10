package cura.objects;

import org.sikuli.script.Pattern;

public class Home {

    public static class Menu {

        public static Pattern history = new Pattern("./src/main/resources/imgs/home_menu_history.png");
        public static Pattern login = new Pattern("./src/main/resources/imgs/home_menu_login.png");
        public static Pattern logout = new Pattern("./src/main/resources/imgs/home_menu_logout.png");
        public static Pattern toggle = new Pattern("./src/main/resources/imgs/home_menu_toggle.png");
    }

    public static Pattern appointment_button = new Pattern("./src/main/resources/imgs/home_appointment_button.png");
    public static Pattern title = new Pattern("./src/main/resources/imgs/home_title.png");
    public static String url = "http://demoaut.katalon.com/";
}
