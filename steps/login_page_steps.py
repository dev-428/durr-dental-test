import time
from selenium import webdriver
from pages.login_page import LoginPage
from behave import given, when, then


@then("I fill in my email and password")
def fill_email_and_password(context):
    email = context.config.userdata.get('email')
    password = context.config.userdata.get('password')
    login_page = LoginPage(context.driver)
    login_page.fill_email_field(email)
    login_page.fill_password_field(password)

@then("Click the login button")
def click_login_button(context):
    login_page = LoginPage(context.driver)
    login_page.click_login_button()
    time.sleep(10)
