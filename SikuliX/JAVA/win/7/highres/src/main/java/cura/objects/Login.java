package cura.objects;

import org.sikuli.script.Pattern;

public class Login {

    public static class Form {

        public static Pattern password = new Pattern("imgs/password_field.png");
        public static Pattern submit = new Pattern("imgs/submit.png");
        public static Pattern username = new Pattern("imgs/username_field.png");
    }

    public static Pattern failed = new Pattern("imgs/login_failed.png");
    public static String url = "http://demoaut.katalon.com/profile.php#login";
}
