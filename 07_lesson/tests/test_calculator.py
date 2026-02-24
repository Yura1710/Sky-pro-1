from pages.calculator_page import CalculatorPage


def test_slow_calculator(browser):
    

    
    calc_page = CalculatorPage(browser)

    
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    
    calc_page.set_delay(45)

    
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    
    assert calc_page.wait_for_result(15), "Результат 15 не появился в течение 50 секунд"

    
    result_text = calc_page.get_result()
    assert result_text == "15", f"Ожидалось '15', получено '{result_text}'"