from helpers.selenium_helper import SeleniumHelper

class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelper(self.driver)

    def get_current_page_url(self, url: str) -> str:
        """
        Get current page url.

        Returns:
            Current page url.
        """
        
        self.helper.confirm_url_to_be(url)
        return self.driver.current_url
