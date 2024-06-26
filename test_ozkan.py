import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestGoogleSearch:
    @classmethod
    def setup_class(cls):
        # Initialize WebDriver
        cls.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):

        cls.driver.quit()

    def test_google_search(self):

        self.driver.get("https://www.google.com/")

if __name__ == "__main__":
    pytest.main()
