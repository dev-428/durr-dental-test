import time
from selenium import webdriver
from pages.welcome_page import WelcomePage
from behave import given, when, then


@given('I open VistaSoft Monitor on my browser')
def open_vistasoft_monitor(context):
    url = context.config.userdata.get('VistaSoftMonitorWelcomePageLink')
    context.driver.get(url)
    time.sleep(5)

@then('I click on the Login button')
def click_login_button(context):
    welcome_page = WelcomePage(context.driver)
    welcome_page.click_login_button()
    time.sleep(5)