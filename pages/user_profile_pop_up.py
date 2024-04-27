from helpers.selenium_helper import SeleniumHelper


# locators
MY_USER_ACCOUNT_BUTTON_LOCATOR = "//div[@id='user-profile']"
LANGUAGE_BUTTON_LOCATOR = "//div[@id='language']"
HELP_BUTTON_LOCATOR = "//div[@id='help']"
LEGAL_BUTTON_LOCATOR = "//div[@id='legal']"
LOG_OUT_BUTTON_LOCATOR = "//div[@id='logout']"


class UserProfilePopUp():

    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(self.driver)

    def _verify_page_element(self) -> None:
        """
        Verify page elements are present.
        """

        self.helper.confirm_presence_of_element_by_xpath(MY_USER_ACCOUNT_BUTTON_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(LANGUAGE_BUTTON_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(HELP_BUTTON_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(LEGAL_BUTTON_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(LOG_OUT_BUTTON_LOCATOR)
    
    def click_my_user_account_button(self) -> None:
        """
        Clicks the "My user account" button in the user profile pop up.
        """

        self.helper.click_element(MY_USER_ACCOUNT_BUTTON_LOCATOR)
