package cura.testcases;

import cura.objects.AppointmentConfirm;
import cura.objects.AppointmentForm;
import cura.objects.Home;
import cura.objects.Login;
import org.apache.http.util.Asserts;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.sikuli.script.FindFailed;
import org.sikuli.script.Region;
import org.sikuli.script.Screen;

import java.util.Random;

public class TC_02 {

    private static WebDriver driver;
    private static Region region;

    @Before
    public void setUp() {
        Screen screen = new Screen(0);
        region = new Region(screen.getBounds());
        System.setProperty("webdriver.chrome.driver", "src/main/resources/chromedriver.exe");
        driver = new ChromeDriver();
    }

    @After
    public void tearDown() {
        driver.quit();
    }

    @Test
    public void test_A_Bad_User_Cannot_Login() throws FindFailed {

        driver.get(Home.url);
        driver.manage().window().maximize();
        region.wait(Home.title);
        region.click(Home.Menu.toggle);
        region.wait(Home.Menu.login);
        region.click(Home.Menu.login);
        region.wait(Login.Form.username, 30);
        region.paste(Login.Form.username, "Jane Doe");
        region.paste(Login.Form.password, "ThisIsAPassword");
        region.click(Login.Form.submit);
        region.wait(Login.failed, 30);
    }

    @Test
    public void test_B_User_Can_Login() throws FindFailed {

        driver.get(Home.url);
        driver.manage().window().maximize();
        region.wait(Home.title);
        region.click(Home.Menu.toggle);
        region.wait(Home.Menu.login);
        region.click(Home.Menu.login);
        region.wait(Login.Form.username, 30);
        region.paste(Login.Form.username, "John Doe");
        region.paste(Login.Form.password, "ThisIsNotAPassword");
        region.click(Login.Form.submit);
        region.wait(AppointmentForm.title, 30);
    }
}
