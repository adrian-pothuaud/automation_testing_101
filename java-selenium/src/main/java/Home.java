import org.openqa.selenium.By;

public class Home {
    public static String url = "http://demoaut.katalon.com/";
    public static class title {
        public static By selector = new By.ByCssSelector("h1");
        public static String text = "CURA Healthcare Service";
    }
}
