package cura.testcases;

import cura.objects.*;
import org.junit.After;
import org.junit.Before;
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
    public void test_A_User_Can_Create_Appointment() throws FindFailed {

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
        region.click(AppointmentForm.facility);
        region.wait(0.5);
        Random rand1 = new Random();
        int rnd1 = rand1.nextInt() % 3;
        region.type(AppointmentForm.facility_values.get(rnd1));
        region.wait(0.5);
        region.getCenter().click();
        region.wait(0.5);
        Random rand2 = new Random();
        boolean rnd2 = rand2.nextBoolean();
        if (rnd2) {
            region.click(AppointmentForm.apply_readmission);
        }
        Random rand3 = new Random();
        int rnd3 = rand3.nextInt() % 3;
        region.click(AppointmentForm.healthcare_programs.get(rnd3));
        Random rand4 = new Random();
        int rnd_year = rand4.nextInt() % 2021;
        int rnd_month = rand4.nextInt() % 13;
        int rnd_day = rand4.nextInt() % 32;
        region.paste(AppointmentForm.visit_date, rnd_day + "/" + rnd_month + "/" + rnd_year);
        region.paste(AppointmentForm.comment, "Automated test");
        region.click(AppointmentForm.book);
        region.wait(AppointmentConfirm.title, 30);
    }

    @Test
    public void test_B_User_Have_Element_In_History_After_Appointment_Creation() throws FindFailed {

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
        region.click(AppointmentForm.facility);
        region.wait(0.5);
        Random rand1 = new Random();
        int rnd1 = rand1.nextInt() % 3;
        region.type(AppointmentForm.facility_values.get(rnd1));
        region.wait(0.5);
        region.getCenter().click();
        region.wait(0.5);
        Random rand2 = new Random();
        boolean rnd2 = rand2.nextBoolean();
        if (rnd2) {
            region.click(AppointmentForm.apply_readmission);
        }
        Random rand3 = new Random();
        int rnd3 = rand3.nextInt() % 3;
        region.click(AppointmentForm.healthcare_programs.get(rnd3));
        Random rand4 = new Random();
        int rnd_year = rand4.nextInt() % 2021;
        int rnd_month = rand4.nextInt() % 13;
        int rnd_day = rand4.nextInt() % 32;
        region.paste(AppointmentForm.visit_date, rnd_day + "/" + rnd_month + "/" + rnd_year);
        region.paste(AppointmentForm.comment, "Automated test");
        region.click(AppointmentForm.book);
        region.wait(AppointmentConfirm.title, 30);
        region.click(Home.Menu.toggle);
        region.wait(Home.Menu.history);
        region.click(Home.Menu.history);
        region.wait(History.title);
        assert region.findAll(History.element).hasNext();
    }
}
