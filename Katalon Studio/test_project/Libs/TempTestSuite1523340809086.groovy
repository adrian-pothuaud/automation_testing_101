import com.kms.katalon.core.logging.KeywordLogger
import com.kms.katalon.core.exception.StepFailedException
import com.kms.katalon.core.reporting.ReportUtil
import com.kms.katalon.core.main.TestCaseMain
import com.kms.katalon.core.testdata.TestDataColumn
import groovy.lang.MissingPropertyException
import com.kms.katalon.core.testcase.TestCaseBinding
import com.kms.katalon.core.driver.internal.DriverCleanerCollector
import com.kms.katalon.core.model.FailureHandling
import com.kms.katalon.core.configuration.RunConfiguration
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData

Map<String, String> suiteProperties = new HashMap<String, String>();


suiteProperties.put('id', 'Test Suites/TS_RegressionTest')

suiteProperties.put('name', 'TS_RegressionTest')

suiteProperties.put('description', '')
 

DriverCleanerCollector.getInstance().addDriverCleaner(new com.kms.katalon.core.webui.contribution.WebUiDriverCleaner())
DriverCleanerCollector.getInstance().addDriverCleaner(new com.kms.katalon.core.mobile.contribution.MobileDriverCleaner())



RunConfiguration.setExecutionSettingFile("C:\\Users\\apd2\\Documents\\GitHub\\automation_testing_101\\Katalon Studio\\test_project\\Reports\\TS_RegressionTest\\20180410_081329\\execution.properties")

TestCaseMain.beforeStart()

TestCaseMain.startTestSuite('Test Suites/TS_RegressionTest', suiteProperties, [new TestCaseBinding('Test Cases/Main Test Cases/TC1_Verify Successful Login', 'Test Cases/Main Test Cases/TC1_Verify Successful Login',  null), new TestCaseBinding('Test Cases/Main Test Cases/TC2_Verify Successful Appointment', 'Test Cases/Main Test Cases/TC2_Verify Successful Appointment',  null)])
