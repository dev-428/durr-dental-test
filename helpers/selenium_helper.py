from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


WEB_DRIVER_WAIT_TIMEOUT = 10


class SeleniumHelper:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, WEB_DRIVER_WAIT_TIMEOUT)

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
    
    def click_element(self, locator: str) -> None:
        """
        Clicks on a web element located using the provided XPATH locator.

        Args:
            locator: The XPATH locator string for the element.

        Returns:
            None
        """

        self.confirm_presence_of_element_by_xpath(locator)
        element = self.confirm_element_is_clickable_by_xpath(locator)
        element.click()
