package cura.testcases;

import cura.objects.AppointmentConfirm;
import cura.objects.AppointmentForm;
import cura.objects.Home;
import cura.objects.Login;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.sikuli.script.FindFailed;
import org.sikuli.script.Region;
import org.sikuli.script.Screen;

import java.util.Random;

public class TC_01 {

    private static WebDriver driver;
    private static Region region;

    @BeforeClass
    public static void setUp() {
        Screen screen = new Screen(0);
        region = new Region(screen.getBounds());
        System.setProperty("webdriver.chrome.driver", "src/main/resources/chromedriver.exe");
        driver = new ChromeDriver();
    }

    @AfterClass
    public static void tearDown() {
        driver.quit();
    }

    @Test
    public void test_A_Navigate_Home_Page() throws FindFailed {

        driver.get(Home.url);
        driver.manage().window().maximize();
        region.wait(Home.title);
    }

    @Test
    public void test_B_Navigate_Login_Page() throws FindFailed {

        region.click(Home.Menu.toggle);
        region.wait(Home.Menu.login);
        region.click(Home.Menu.login);
        region.wait(Login.Form.username, 30);
    }

    @Test
    public void test_C_Fill_Login_Form() throws FindFailed {

        region.paste(Login.Form.username, "John Doe");
        region.paste(Login.Form.password, "ThisIsNotAPassword");
        region.click(Login.Form.submit);
        region.wait(AppointmentForm.title, 30);
    }

    @Test
    public void test_D_Create_Appointment() throws FindFailed {

        region.click(AppointmentForm.facility);
        region.wait(0.5);
        Random rand = new Random();
        int rnd1 = rand.nextInt((2 - 0) + 1);
        region.type(AppointmentForm.facility_values.get(rnd1));
        region.wait(0.5);
        region.getCenter().click();
        region.wait(0.5);
        Random rand1 = new Random();
        boolean rnd2 = rand1.nextBoolean();
        if (rnd2) {
            region.click(AppointmentForm.apply_readmission);
        }
        Random rand2 = new Random();
        int rnd3 = rand2.nextInt((2 - 0) + 1);
        region.click(AppointmentForm.healthcare_programs.get(rnd3));
        Random rand3 = new Random();
        int year = rand3.nextInt((1950 - 2000) + 1) + 1950;
        int month = rand3.nextInt((1 - 12) + 1) + 1;
        int day = rand3.nextInt((1 - 31) + 1) + 31;
        region.paste(AppointmentForm.visit_date, day + "/" + month + "/" + year);
        region.paste(AppointmentForm.comment, "Automated test");
        region.click(AppointmentForm.book);
        region.wait(AppointmentConfirm.title, 30);
    }
}
