from helpers.selenium_helper import SeleniumHelper
from pages.base_page import BasePage
from pages.left_menu_component import LeftMenuComponent


# locators
DASHBOARD_HEADER_LOCATOR = "//h2[contains(text(), 'Dashboard')]"


class DashboardPage(BasePage, LeftMenuComponent):

    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(self.driver)
        self._verify_page_elements()
    
    def _verify_page_elements(self) -> None:
        """
        Verify page elements are present.
        """

        self.helper.confirm_presence_of_element_by_xpath(DASHBOARD_HEADER_LOCATOR)
    
    def get_header_text(self) -> str:
        """
        Get current page header text.

        Returns:
            Current page header text
        """

        return self.helper.get_element_text_by_xpath(DASHBOARD_HEADER_LOCATOR)
