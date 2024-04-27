class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def get_current_page_url(self) -> str:
        """
        Get current page url.

        Returns:
            Current page url.
        """

        return self.driver.current_url
