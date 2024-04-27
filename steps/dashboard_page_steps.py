from pages.dashboard_page import DashboardPage
from behave import given, when, then


@then("I verify I am at the Dashboard page")
def verify_at_dashboard_page(context):
    dashboard_page = DashboardPage(context.driver)

    header_text = dashboard_page.get_header_text()
    current_page_url = dashboard_page.get_current_page_url(context.config.userdata.get("DashboardPageLink"))

    assert header_text == "Dashboard", "Dashboard header text is incorrect"
    assert current_page_url == context.config.userdata.get("DashboardPageLink"), "Current page url is not Dashboard page url"
