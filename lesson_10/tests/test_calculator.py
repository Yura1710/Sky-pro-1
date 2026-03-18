import allure
from pages.calculator_page import CalculatorPage


@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
class TestSlowCalculator:

    @allure.title("Test slow calculator with 45 seconds delay")
    @allure.description("Test checks that 7 + 8 = 15 after 45 seconds delay")
    def test_slow_calculator(self, browser):
        with allure.step("Open calculator page"):
            browser.get(
                "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
            calc_page = CalculatorPage(browser)

        with allure.step("Set delay to 45 seconds"):
            calc_page.set_delay(45)

        with allure.step("Press buttons: 7, +, 8, ="):
            calc_page.click_button("7")
            calc_page.click_button("+")
            calc_page.click_button("8")
            calc_page.click_button("=")

        with allure.step("Wait for result 15"):
            assert calc_page.wait_for_result(
                15
            ), "Result 15 did not appear in 50 seconds"

        with allure.step("Verify result is 15"):
            result_text = calc_page.get_result()
            assert result_text == "15", f"Expected '15', got '{result_text}'"
