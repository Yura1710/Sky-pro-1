from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")

    def fill_checkout_info(self, first_name, last_name, postal_code):

        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME_INPUT))

        self.input_text(self.FIRST_NAME_INPUT, first_name)
        self.input_text(self.LAST_NAME_INPUT, last_name)
        self.input_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click_element(self.CONTINUE_BUTTON)

        self.wait.until(EC.presence_of_element_located(self.TOTAL_LABEL))

    def get_total(self):

        total_text = self.get_text(self.TOTAL_LABEL)
        return total_text.replace("Total: ", "")

    def finish_order(self):

        self.click_element(self.FINISH_BUTTON)
