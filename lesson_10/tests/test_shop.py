import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Shop")
@allure.severity(allure.severity_level.NORMAL)
class TestShop:

    @allure.title("Test shopping flow")
    @allure.description("Test adding items to cart and checkout")
    def test_shop(self, browser):
        with allure.step("Open login page"):
            browser.get("https://www.saucedemo.com/")
            login_page = LoginPage(browser)

        with allure.step("Login as standard_user"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Add items to cart"):
            inventory_page = InventoryPage(browser)
            inventory_page.add_backpack()
            inventory_page.add_bolt_tshirt()
            inventory_page.add_onesie()

        with allure.step("Go to cart"):
            inventory_page.go_to_cart()
            cart_page = CartPage(browser)

        with allure.step("Proceed to checkout"):
            cart_page.go_to_checkout()
            checkout_page = CheckoutPage(browser)

        with allure.step("Fill checkout information"):
            checkout_page.fill_checkout_info("Иван", "Петров", "123456")

        with allure.step("Verify total price"):
            total = checkout_page.get_total()
            expected_total = "$58.29"
            assert total == expected_total, (
                f"Expected {expected_total}, got {total}"
            )

        with allure.step("Finish order"):
            checkout_page.finish_order()
