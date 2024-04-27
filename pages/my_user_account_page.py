from helpers.selenium_helper import SeleniumHelper
from pages.base_page import BasePage
from pages.left_menu_component import LeftMenuComponent


# locators
MY_USER_ACCOUNT_HEADER_LOCATOR = "//span[contains(text(), 'My user account')]"
EDITING_USER_DATA_HEADER_LOCATOR = "//h3[contains(text(), 'Editing user data')]"
FIRST_NAME_FIELD_LOCATOR = "//input[@id='firstName']"
LAST_NAME_FIELD_LOCATOR = "//input[@id='lastName']"
EMAIL_FIELD_LOCATOR = "//input[@id='email']"
SUPPORT_EMAIL_LOCATOR = "//a[contains(text(), 'support-vsm@duerrdental.com')]"
DELETE_USER_ACCOUNT_HEADER_LOCATOR = "//h3[contains(text(), 'Delete user account')]"
DELETE_USER_ACCOUNT_BUTTON_LOCATOR = "//button/span[contains(text(), 'Delete user account irrevocably')]"


class MyUserAccount(BasePage, LeftMenuComponent):

    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(self.driver)

    def _verify_page_elements(self) -> None:
        """
        Verify page elements are present.
        """

        self.helper.confirm_presence_of_element_by_xpath(MY_USER_ACCOUNT_HEADER_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(EDITING_USER_DATA_HEADER_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(FIRST_NAME_FIELD_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(LAST_NAME_FIELD_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(EMAIL_FIELD_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(SUPPORT_EMAIL_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(DELETE_USER_ACCOUNT_HEADER_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(DELETE_USER_ACCOUNT_BUTTON_LOCATOR)

    def get_header_text(self) -> str:
        """
        Get current page header text.

        Returns:
            Current page header text
        """

        return self.helper.get_element_text_by_xpath(MY_USER_ACCOUNT_HEADER_LOCATOR)
    
    def get_first_name_text(self) -> str:
        """
        Get first name text.

        Returns:
            First name text
        """

        return self.helper.get_disabled_element_text_by_xpath(FIRST_NAME_FIELD_LOCATOR)
    
    def get_last_name_text(self) -> str:
        """
        Get last name text.

        Returns:
            Last name text
        """

        return self.helper.get_disabled_element_text_by_xpath(LAST_NAME_FIELD_LOCATOR)
    
    def get_email_text(self) -> str:
        """
        Get email text.

        Returns:
            Email text
        """

        return self.helper.get_disabled_element_text_by_xpath(EMAIL_FIELD_LOCATOR)
