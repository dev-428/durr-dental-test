from helpers.selenium_helper import SeleniumHelper


# locators
HEADER_LOCATOR = "//h1[contains(text(), ' A clear view of everything with VistaSoft Monitor')]"
VISTASOFT_MONITOR_LINK_LOCATOR = "//a[contains(text(), 'VistaSoft Monitor')]"
LOGIN_BUTTON_LOCATOR = "//button/span/span[contains(text(), 'Login')]"


class WelcomePage():
    
    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(self.driver)
        self._verify_page_elements()
    
    def _verify_page_elements(self) -> None:
        """
        Verify page elements are present.
        """
        
        self.helper.confirm_presence_of_element_by_xpath(HEADER_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(VISTASOFT_MONITOR_LINK_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(LOGIN_BUTTON_LOCATOR)
    
    def click_login_button(self) -> None:
        """
        Click the login button.
        """
        
        self.helper.click_element(LOGIN_BUTTON_LOCATOR)
