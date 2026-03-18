from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):
    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT_ADD = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self):
        self.click_element(self.BACKPACK_ADD)

    def add_bolt_tshirt(self):
        self.click_element(self.TSHIRT_ADD)

    def add_onesie(self):
        self.click_element(self.ONESIE_ADD)

    def get_cart_count(self):
        try:
            element = self.driver.find_element(*self.CART_BADGE)
            return int(element.text)
        except Exception:
            return 0

    def go_to_cart(self):
        self.click_element(self.CART_LINK)
        self.wait.until(lambda driver: "cart" in driver.current_url)
