package com.apothuaud;

import org.testng.annotations.Test;

import com.consol.citrus.annotations.CitrusXmlTest;
import com.consol.citrus.testng.AbstractTestNGCitrusTest;

/**
 * Login process tests. Valid User can Login, Invalid User cannot.
 *
 * @author apothuaud
 * @since 2018-04-11
 */
@Test
public class CURATC01Login extends AbstractTestNGCitrusTest {

    @CitrusXmlTest(name = "CURATC01Login")
    public void cURATC01Login() {}
}
