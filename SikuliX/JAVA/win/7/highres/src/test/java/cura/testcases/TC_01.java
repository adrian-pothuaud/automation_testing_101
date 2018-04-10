package cura.testcases;

import cura.objects.Home;
import junit.framework.TestCase;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.sikuli.script.FindFailed;
import org.sikuli.script.Region;
import org.sikuli.script.Screen;

public class TC_01 {

    private WebDriver driver;
    private Screen screen;
    private Region region;

    @Before
    public void setUp() {
        screen = new Screen(0);
        region = new Region(screen.getBounds());
        System.setProperty("webdriver.chrome.driver", "src/main/resources/chromedriver.exe");
        driver = new ChromeDriver();
    }

    @Test
    public void test_A_Navigate_Home_Page() throws FindFailed {

        driver.get(Home.url);
        region.wait(Home.title);
    }
}
