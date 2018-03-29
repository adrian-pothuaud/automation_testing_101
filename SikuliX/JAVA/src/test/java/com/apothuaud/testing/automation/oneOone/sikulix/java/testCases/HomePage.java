package com.apothuaud.testing.automation.oneOone.sikulix.java.testCases;

import org.junit.BeforeClass;
import org.junit.Test;
import org.sikuli.script.FindFailed;

import java.awt.*;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class HomePage {

    @SuppressWarnings("FieldCanBeLocal")
    private static Path path;
    private static org.sikuli.script.Screen s0;

    @BeforeClass
    public static void setUpClass() {

        path = Paths.get("src", "main", "resources", "images", "home");
        org.sikuli.script.ImagePath.add(path.toString());
        s0 = new org.sikuli.script.Screen(0);
    }

    @Test
    public void test_A_HomePage_Have_SeleniumHQ_Image() throws URISyntaxException, IOException, FindFailed {

        Desktop desktop = java.awt.Desktop.getDesktop();
        URI oURL = new URI("https://www.seleniumhq.org/");
        System.out.println("URL is set to " + oURL + ".");
        desktop.browse(oURL);
        System.out.println("Browser openned to URL.");
        System.out.println("On Screen " + s0);
        org.sikuli.script.Pattern img1 = new org.sikuli.script.Pattern("seleniumhq.png");
        System.out.println("waiting for img " + img1);
        s0.wait(img1, 30);
        System.out.println("Image found !");
    }

    @Test
    public void test_B_Verify_HomePage_Footer() throws FindFailed, URISyntaxException, IOException {

        Desktop desktop = java.awt.Desktop.getDesktop();
        URI oURL = new URI("https://www.seleniumhq.org/");
        System.out.println("URL is set to " + oURL + ".");
        desktop.browse(oURL);
        System.out.println("Browser openned to URL.");
        s0.wait(2.0);
        int wheel_direction;
        //noinspection deprecation
        if (org.sikuli.script.Env.isWindows()) {
            wheel_direction = 1;
        } else {
            wheel_direction = -1;
        }
        s0.getCenter().click();
        s0.wait(1.0);
        s0.wheel(wheel_direction, 50);
        System.out.println("Scroll down to bottom.");
        System.out.println("On Screen " + s0);
        org.sikuli.script.Pattern img2 = new org.sikuli.script.Pattern("footer.png");
        System.out.println("waiting for img " + img2);
        s0.wait(img2, 30);
        System.out.println("Image found !");
    }
}
