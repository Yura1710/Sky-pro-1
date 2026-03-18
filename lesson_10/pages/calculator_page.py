from selenium.webdriver.common.by import By
from .base_page import BasePage
from typing import Tuple


class CalculatorPage(BasePage):
    DELAY_INPUT: Tuple[str, str] = (By.CSS_SELECTOR, "#delay")
    RESULT_SCREEN: Tuple[str, str] = (By.CSS_SELECTOR, ".screen")

    @staticmethod
    def _button_locator(text: str) -> Tuple[str, str]:
        return (By.XPATH, f"//span[text()='{text}']")

    def set_delay(self, seconds: int) -> None:
        self.input_text(self.DELAY_INPUT, str(seconds))

    def click_button(self, button_text: str) -> None:
        self.click_element(self._button_locator(button_text))

    def get_result(self) -> str:
        return self.get_text(self.RESULT_SCREEN)

    def wait_for_result(self, expected_result: int, timeout: int = 50) -> bool:
        from selenium.webdriver.support import expected_conditions as EC
        self.wait._timeout = timeout
        return self.wait.until(
            EC.text_to_be_present_in_element(
                self.RESULT_SCREEN, str(expected_result)
            )
        )
