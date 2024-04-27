from helpers.selenium_helper import SeleniumHelper


# locators
DASHBOARD_LEFT_MENU_BUTTON_LOCATOR = "(//span[contains(text(), 'Dashboard')])[2]"
INBOX_LEFT_MENU_BUTTON_LOCATOR = "(//span[contains(text(), 'Inbox')])[2]"
MY_DEVICES_LEFT_MENU_BUTTON_LOCATOR = "(//span[contains(text(), 'My devices')])[2]"
PRODUCT_SEARCH_LEFT_MENU_BUTTON_LOCATOR = "(//span[contains(text(), 'Product search')])[2]"
SAVED_DOCUMENTS_LEFT_MENU_BUTTON_LOCATOR = "(//span[contains(text(), 'Saved documents')])[2]"
PRODUCT_REGISTRATION_LEFT_MENU_BUTTON_LOCATOR = "(//span[contains(text(), 'Product registration 2+1')])[2]"
SETTINGS_LEFT_MENU_BUTTON_LOCATOR = "(//span[contains(text(), 'Settings')])[2]"
USER_PROFILE_BUTTON_LOCATOR = "(//div[@aria-label='nav-user-button'])[2]"


class LeftMenuComponent():

    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(self.driver)
        self._verify_page_elements()

    def _verify_page_elements(self) -> None:
        """
        Verify page elements are present.
        """

        self.helper.confirm_presence_of_element_by_xpath(DASHBOARD_LEFT_MENU_BUTTON_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(INBOX_LEFT_MENU_BUTTON_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(MY_DEVICES_LEFT_MENU_BUTTON_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(PRODUCT_SEARCH_LEFT_MENU_BUTTON_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(SAVED_DOCUMENTS_LEFT_MENU_BUTTON_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(PRODUCT_REGISTRATION_LEFT_MENU_BUTTON_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(SETTINGS_LEFT_MENU_BUTTON_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(USER_PROFILE_BUTTON_LOCATOR) 

    def click_dashboard_button(self) -> None:
        """
        Clicks the "Dashboard" button on the left menu.
        """

        self.helper.click_element(DASHBOARD_LEFT_MENU_BUTTON_LOCATOR)

    def click_inbox_button(self) -> None:
        """
        Clicks the "Inbox" button on the left menu.
        """

        self.helper.click_element(INBOX_LEFT_MENU_BUTTON_LOCATOR)

    def click_my_devices_button(self) -> None:
        """
        Clicks the "My Devices" button on the left menu.
        """
        
        self.helper.click_element(MY_DEVICES_LEFT_MENU_BUTTON_LOCATOR)

    def click_product_search_button(self) -> None:
        """
        Clicks the "Product search" button on the left menu.
        """

        self.helper.click_element(PRODUCT_SEARCH_LEFT_MENU_BUTTON_LOCATOR)

    def click_saved_documents_button(self) -> None:
        """
        Clicks the "Saved documents" button on the left menu.
        """

        self.helper.click_element(SAVED_DOCUMENTS_LEFT_MENU_BUTTON_LOCATOR)

    def click_product_registration_button(self) -> None:
        """
        Clicks the "Product registration 2+1" button on the left menu.
        """

        self.helper.click_element(PRODUCT_REGISTRATION_LEFT_MENU_BUTTON_LOCATOR)

    def click_settings_button(self) -> None:
        """
        Clicks the "Settings" button on the left menu.
        """

        self.helper.click_element(SETTINGS_LEFT_MENU_BUTTON_LOCATOR)

    def click_user_profile_button(self) -> None:
        """
        Clicks the "User Navigation" button of the left menu.
        
        This is located all the way at the bottom with username and email. 
        """

        self.helper.click_element(USER_PROFILE_BUTTON_LOCATOR)
