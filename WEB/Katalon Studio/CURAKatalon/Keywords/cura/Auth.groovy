package cura

import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject

import com.kms.katalon.core.annotation.Keyword
import com.kms.katalon.core.checkpoint.Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords
import com.kms.katalon.core.model.FailureHandling
import com.kms.katalon.core.testcase.TestCase
import com.kms.katalon.core.testcase.TestCaseFactory
import com.kms.katalon.core.testdata.TestData
import com.kms.katalon.core.testdata.TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository
import com.kms.katalon.core.testobject.TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords

import internal.GlobalVariable

import MobileBuiltInKeywords as Mobile
import WSBuiltInKeywords as WS
import WebUiBuiltInKeywords as WebUI

public class Auth {
	
	@Keyword
	def login(username, password) {
		WebUI.openBrowser("http://demoaut.katalon.com/profile.php#login")
		WebUI.maximizeWindow()
		WebUI.waitForElementPresent(findTestObject("Page_CURA Healthcare Service/input_username"), 3)
		WebUI.sendKeys(findTestObject("Page_CURA Healthcare Service/input_username"), username)
		WebUI.sendKeys(findTestObject("Page_CURA Healthcare Service/input_password"), password)
		WebUI.click(findTestObject("Page_CURA Healthcare Service/button_Login"))
	}
}
