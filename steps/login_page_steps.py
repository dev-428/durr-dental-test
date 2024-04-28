import os
from pages.login_page import LoginPage
from behave import given, when, then
from dotenv import load_dotenv


load_dotenv("config.env")
LARRY_USER_EMAIL = os.getenv("LARRY_USER_EMAIL")
LARRY_USER_PASSWORD = os.getenv("LARRY_USER_PASSWORD")


@then("I login as user Larry on the login page")
def login_as_user_larry(context):
    login_page = LoginPage(context.driver)
    login_page.fill_email_field(LARRY_USER_EMAIL)
    login_page.fill_password_field(LARRY_USER_PASSWORD)


@then("I click on the LOG-IN button on the login page")
def click_login_button_login_page(context):
    login_page = LoginPage(context.driver)
    login_page.click_login_button()
