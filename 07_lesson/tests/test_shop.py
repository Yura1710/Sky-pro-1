def test_shop(browser):

    from pages.login_page import LoginPage
    from pages.inventory_page import InventoryPage
    from pages.cart_page import CartPage
    from pages.checkout_page import CheckoutPage

    browser.get("https://www.saucedemo.com/")

    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_backpack()
    inventory_page.add_bolt_tshirt()
    inventory_page.add_onesie()

    inventory_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(browser)
    checkout_page.fill_checkout_info("Иван", "Петров", "123456")

    total = checkout_page.get_total()
    expected_total = "$58.29"

    assert total == expected_total, (
        f"Ожидалось {expected_total}, получено {total}"
    )

    checkout_page.finish_order()
