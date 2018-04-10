package cura.objects;

import org.sikuli.script.Pattern;

public class Login {

    public static class Form {

        public static Pattern password = new Pattern("src/main/resources/imgs/login_password.png");
        public static Pattern submit = new Pattern("src/main/resources/imgs/login_submit.png");
        public static Pattern username = new Pattern("src/main/resources/imgs/login_username.png");
    }

    public static Pattern failed = new Pattern("src/main/resources/imgs/login_failed.png");
    public static String url = "http://demoaut.katalon.com/profile.php#login";
}
