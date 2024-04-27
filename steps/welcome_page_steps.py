from pages.welcome_page import WelcomePage
from behave import given, when, then


@given("I open VistaSoft Monitor welcome page on my browser")
def open_vistasoft_monitor_welcome_page_on_browser(context):
    url = context.config.userdata.get("VistaSoftMonitorWelcomePageLink")
    context.driver.get(url)

@when("I click Login button on the welcome page")
def click_login_button_welcome_page(context):
    welcome_page = WelcomePage(context.driver)
    welcome_page.click_login_button()