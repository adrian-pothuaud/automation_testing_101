package cura;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class Login {
    private static By username_field = new By.ById("txt-username");
    private static By password_field = new By.ById("txt-password");
    private static By submit = new By.ById("btn-login");
    public static By failure = new By.ByClassName("text-danger");

    // Methods
    /**
     * Open Login Page.
     * @param driver A WebDriver instance to handle actions.
     * @see WebDriver
     */
    public static void open(WebDriver driver) {
        /*
      CURA Login Page Object.
      Represents Login Form.
      Contains methods to open the page and fill Login Form.
     */
        String url = "http://demoaut.katalon.com/profile.php#login";
        driver.get(url);
        driver.manage().window().maximize();
    }

    /**
     * Fill Login form and validate.
     * @param driver A WebDriver instance for action handling.
     * @param username For credentials.
     * @param password For credentials.
     * @see WebDriver
     */
    private static void fillForm(WebDriver driver, String username, String password) {
        driver.findElement(username_field).sendKeys(username);
        driver.findElement(password_field).sendKeys(password);
        driver.findElement(submit).click();
    }

    /**
     * Fill Login form and validate.
     * @param driver A WebDriver instance for action handling.
     * @param user A User instance for credentials.
     * @see WebDriver
     * @see User
     */
    public static void fillForm(WebDriver driver, User user) {
        fillForm(driver, user.getUsername(), user.getPassword());
    }
}
