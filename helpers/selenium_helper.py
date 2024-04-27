from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


WEB_DRIVER_WAIT_TIMEOUT = 30


class SeleniumHelper:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, WEB_DRIVER_WAIT_TIMEOUT)

    def confirm_url_to_be(self, expected_url: str) -> None:
        """
        Waits for the current page url to match the expected url.

        Args:
            expected_url: The url you expect the current page to have.
        
        Returns:
            None
        """

        self.wait.until(EC.url_to_be(expected_url))

    def confirm_presence_of_element_by_xpath(self, locator: str) -> WebElement:
        """
        Waits for the presence of a web element on the page using an XPATH locator.

        Args:
            locator: The XPATH locator string for the element.
        
        Returns:
            WebElement: WebElement object if the element is found.
        """
        
        return self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
    
    def confirm_element_is_clickable_by_xpath(self, locator: str) -> WebElement:
        """
        Waits for a web element located using an XPATH locator to become clickable.

        Args:
            locator: The XPATH locator string for the element.

        Returns:
            WebElement: WebElement object if the element is found.
        """

        return self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
    
    def get_element_text_by_xpath(self, locator: str) -> str:
        """
        Get web element text using the provided XPATH locator.

        Args:
            locator: The XPATH locator string for the element.

        Returns:
            Web element text
        """

        self.confirm_presence_of_element_by_xpath(locator)
        element = self.driver.find_element(By.XPATH, locator)
        return element.text
    
    def get_disabled_element_text_by_xpath(self, locator: str) -> str:
        """
        Get disabled web element text using the provided XPATH locator.

        Args:
            locator: The XPATH locator string for the disabled element.
        
        Returns:
            Disabled web element text
        """

        self.confirm_presence_of_element_by_xpath(locator)
        element = self.driver.find_element(By.XPATH, locator)
        text = element.get_attribute('value')
        return text

    def click_element(self, locator: str) -> None:
        """
        Clicks on a web element locator using the provided XPATH locator.

        Args:
            locator: The XPATH locator string for the element.

        Returns:
            None
        """

        self.confirm_presence_of_element_by_xpath(locator)
        element = self.confirm_element_is_clickable_by_xpath(locator)
        element.click()

    def fill_element_with_text(self, locator: str, text: str) -> None:
        """
        Fills a web element with the provided text using the given locator.

        Args:
            locator: The XPATH locator string for the element.
            text: The text to enter into the element.
        
        Returns:
            None
        """
        
        element = self.confirm_presence_of_element_by_xpath(locator)
        element.send_keys(text)
    