from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple


class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator: Tuple[str, str]) -> None:
        self.find_element(locator).click()

    def input_text(self, locator: Tuple[str, str], text: str) -> None:
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: Tuple[str, str]) -> str:
        return self.find_element(locator).text
