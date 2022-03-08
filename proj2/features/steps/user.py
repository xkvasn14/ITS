from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

SLEEP_TIME = 2

@given(u'User is at main page')
def step_impl(context):
    pass


@when(u'he clicks on "Log in"')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.set_window_size(1848, 1016)
    context.driver.find_element(By.ID, "personaltools-login").click()


@when(u'fills correctly Name with password')
def step_impl(context):
    context.driver.find_element(By.ID, "__ac_name").click()
    context.driver.find_element(By.ID, "__ac_name").send_keys("itsreviewer")
    context.driver.find_element(By.ID, "__ac_password").send_keys("itsreviewer")


@when(u'clicks on "Log in"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()


@then(u'he should log in')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")


@given(u'the User is at main page')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.set_window_size(924, 1016)



@when(u'he tries to open header "Use Cases"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()


@then(u'the Use Case in the list should not be visible')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/use-cases")


@given(u'User wants to log out')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#portal-logo > img").click()
    time.sleep(SLEEP_TIME)


@when(u'he clicks on "its Reviewer"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
    time.sleep(SLEEP_TIME)


@when(u'clicks on "Log out"')
def step_impl(context):
    context.driver.find_element(By.ID, "personaltools-logout").click()
    time.sleep(SLEEP_TIME)


@then(u'Then he should be logged out')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
