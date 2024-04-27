from pages.user_profile_pop_up import UserProfilePopUp
from behave import given, when, then


@then("I click on My user account button on the User Profile pop up")
def click_my_user_account_button_on_user_profile_pop_up(context):
    user_profile_pop_up = UserProfilePopUp(context.driver)
    user_profile_pop_up.click_my_user_account_button()
