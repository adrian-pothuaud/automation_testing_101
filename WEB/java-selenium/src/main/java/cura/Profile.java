package cura;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class Profile {
    public static By title = new By.ByCssSelector("h1");
    public static By element = new By.ByClassName("panel-info");

    public static void open(WebDriver driver) {
        String url = "http://demoaut.katalon.com/profile.php#profile";
        driver.get(url);
    }

    public static int getNbElements(WebDriver driver) {
        return driver.findElements(element).size();
    }
}
