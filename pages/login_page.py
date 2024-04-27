from helpers.selenium_helper import SeleniumHelper


# locators
PICTURE_TEXT_LOCATOR = "//span[contains(text(), 'My Dürr Dental')]"
PICTURE_HEADER_LOCATOR = "//h1[contains(text(), 'A portal for all your online services and tools.')]"
LOGIN_HEADER_LOCATOR = "//h1[contains(text(), 'Log-in')]"
EMAIL_INPUT_LOCATOR = "//input[@id='username']"
PASSWORD_INPUT_LOCATOR = "//input[@id='password']"
SHOW_PASSWORD_INPUT_LOCATOR = "//button[1]"
LOGIN_BUTTON_LOCATOR = "//button[@name='login']"
FORGOTTEN_PASSWORD_TEXT_LOCATOR = "//div[contains(text(), 'Have you forgotten your password?')]"
PASSWORD_FORGOTTEN_LINK_LOCATOR = "//span[contains(text(), 'Password forgotten')]"
NO_ACCESS_YET_TEXT_LOCATOR = "//div[contains(text(), 'You have no access yet?')]"
SIGN_UP_LINK_LOCATOR = "//span[contains(text(), 'Sign up')]"
CONTACT_TEXT_LOCATOR = "//div[contains(text(), 'Contact')]"
CONTACT_NUMBER_LOCATOR = "//a[contains(text(), '+49 7142 / 705-0')]"
CONTACT_EMAIL_LOCATOR = "//a[contains(text(), 'info@duerrdental.com')]"
ADDRESS_LINE_ONE_LOCATOR = "//span[contains(text(), 'Dürr Dental SE')]"
ADDRESS_LINE_TWO_LOCATOR = "//span[contains(text(), 'Höpfigheimer Str. 17')]"
ADDRESS_LINE_THREE_LOCATOR = "//span[contains(text(), '74321 Bietigheim-Bissingen')]"
DURR_DENTAL_WEBSITE_LINK_LOCATOR = "//span[contains(text(), 'To the website of Dürr Dental')]"
TERMS_AND_CONDITIONS_BUTTON_LOCATOR = "//button[contains(text(), 'Terms and Conditions')]"
DATA_PROTECTION_LINK_LOCATOR = "//a[contains(text(), 'Data Protection')]"


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(self.driver)
        self._verify_page_elements()
    
    def _verify_page_elements(self) -> None:
        """
        Verify page elements are present.s
        """
        
        self.helper.confirm_presence_of_element_by_xpath(PICTURE_TEXT_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(PICTURE_HEADER_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(LOGIN_HEADER_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(EMAIL_INPUT_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(PASSWORD_INPUT_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(SHOW_PASSWORD_INPUT_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(LOGIN_BUTTON_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(FORGOTTEN_PASSWORD_TEXT_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(PASSWORD_FORGOTTEN_LINK_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(NO_ACCESS_YET_TEXT_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(SIGN_UP_LINK_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(CONTACT_TEXT_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(CONTACT_NUMBER_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(CONTACT_EMAIL_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(ADDRESS_LINE_ONE_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(ADDRESS_LINE_TWO_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(ADDRESS_LINE_THREE_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(DURR_DENTAL_WEBSITE_LINK_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(TERMS_AND_CONDITIONS_BUTTON_LOCATOR)
        self.helper.confirm_presence_of_element_by_xpath(DATA_PROTECTION_LINK_LOCATOR)

    def fill_email_field(self, text: str) -> None:
        """
        Fill email input field with given text.

        Args:
            text: Signed up email account
        
        Returns:
            None
        """

        self.helper.fill_element_with_text(EMAIL_INPUT_LOCATOR, text)

    def fill_password_field(self, text: str) -> None:
        """
        Fill password input field with given text.

        Args:
            text: Password associated with signed up email account

        Returns:
            None
        """

        self.helper.fill_element_with_text(PASSWORD_INPUT_LOCATOR, text)
    
    def click_login_button(self) -> None:
        """
        Click login button
        """
        
        self.helper.click_element(LOGIN_BUTTON_LOCATOR)
