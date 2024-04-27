from pages.login_page import LoginPage
from behave import given, when, then


@then("I fill my email and password on the login page")
def fill_email_and_password_on_login_page(context):
    email = context.config.userdata.get('email')
    password = context.config.userdata.get('password')

    login_page = LoginPage(context.driver)
    login_page.fill_email_field(email)
    login_page.fill_password_field(password)

@then("I click on the LOG-IN button on the login page")
def click_login_button_login_page(context):
    login_page = LoginPage(context.driver)
    login_page.click_login_button()
