from lettuce import *
from selenium import webdriver

from objects.Appointment import Form as AppointmentForm
from objects.Login import Page as Login
from objects.Profile import Page as Profile
from objects.Shared import Menu


@before.each_scenario
def setup_some_scenario(scenario):
    world.driver = webdriver.Firefox()


@after.each_scenario
def teardown_some_scenario(scenario):
    world.driver.close()


@step('A valid User')
def valid_user(step):
    world.user = {
        "username": "John Doe",
        "password": "ThisIsNotAPassword"
    }


@step('An invalid User')
def valid_user(step):
    world.user = {
        "username": "Jane Doe",
        "password": "ThisIsAPassword"
    }


@step('I go to Login page')
def go_to_login(step):
    Login.open(world.driver)


@step('I enter User credentials')
def enter_credentials(step):
    Login.fill(world.driver, world.user["username"], world.user["password"])


@step('I should be logged in')
def login_success(step):
    world.driver.find_element_by_css_selector(
        AppointmentForm.title.selector
    )


@step('I should not be logged in')
def login_failure(step):
    world.driver.find_element_by_css_selector(
        Login.failed.selector
    )


@step('I go to Profile page')
def go_to_profile(step):
    Menu.navigate_to(world.driver, "profile")


@step('I should see my Profile')
def see_profile(step):
    world.driver.find_element_by_css_selector(
        Profile.title.selector
    )
