from pages.left_menu_component import LeftMenuComponent
from behave import given, when, then


@then("I click on User Profile button on the left menu component")
def click_user_profile_button_on_left_menu_component(context):
    left_menu_component = LeftMenuComponent(context.driver)
    left_menu_component.click_user_profile_button()
