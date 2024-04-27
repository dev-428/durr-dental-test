from pages.my_user_account_page import MyUserAccount
from behave import given, when, then


@then("I verify I am at the My user account page")
def verify_at_my_user_account_page(context):
    my_user_account_page = MyUserAccount(context.driver)

    header_text = my_user_account_page.get_header_text()
    current_page_url = my_user_account_page.get_current_page_url(context.config.userdata.get("MyUserAccountPageLink"))

    assert header_text == "My user account", "My user account header text is incorrect"
    assert current_page_url == context.config.userdata.get("MyUserAccountPageLink"), "Current page url is not My user account page url"

@then('I verify my first name is "{firstName}" and last name is "{lastName}" at My user account page')
def verify_first_name_and_last_name_at_my_user_account_page(context, firstName, lastName):
    my_user_account_page = MyUserAccount(context.driver)

    assert my_user_account_page.get_first_name_text() == firstName, "First name is incorrect"
    assert my_user_account_page.get_last_name_text() == lastName, "Last name is incorrect"

@then('I verify my "{email}" at My user account page')
def verify_email_at_my_user_account_page(context, email):
    my_user_account_page = MyUserAccount(context.driver)

    assert my_user_account_page.get_email_text() == email, "Email is incorrect"
