import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;

public class tc_CURA_Login {

    @Test
    public void test_User_Can_Login() {

        File file = new File("src/main/resources/bin/geckodriver.exe");
        System.setProperty("webdriver.ie.driver", file.getAbsolutePath());
        WebDriver driver = new FirefoxDriver();
        driver.get(Home.url);
        driver.manage().window().maximize();
        WebDriverWait wait = new WebDriverWait(driver, 10);
        wait.until(ExpectedConditions.visibilityOfElementLocated(Home.title.selector));
    }
}
