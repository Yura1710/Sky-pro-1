from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestSlowCalculator:
    """Тест для проверки медленного калькулятора"""

    def setup_method(self):
        """Настройка браузера перед тестом"""
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        """Закрытие браузера после теста"""
        if self.driver:
            self.driver.quit()

    def test_slow_calculator(self):
        """Тест проверки работы калькулятора с задержкой"""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        print("Страница загружена")

        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")
        print("Задержка установлена на 45 секунд")

        button_7 = self.driver.find_element(By.XPATH, "//span[text()='7']")
        button_7.click()
        print("Нажата кнопка 7")

        button_plus = self.driver.find_element(By.XPATH, "//span[text()='+']")
        button_plus.click()
        print("Нажата кнопка +")

        button_8 = self.driver.find_element(By.XPATH, "//span[text()='8']")
        button_8.click()
        print("Нажата кнопка 8")

        button_equals = self.driver.find_element(
            By.XPATH, "//span[text()='=']"
        )
        button_equals.click()
        print("Нажата кнопка =, ожидаем результат...")

        result_locator = (By.CSS_SELECTOR, ".screen")
        expected_result = "15"

        wait = WebDriverWait(self.driver, 50)
        wait.until(
            EC.text_to_be_present_in_element(result_locator, expected_result)
        )
        print("Результат появился!")

        result_text = self.driver.find_element(*result_locator).text
        assert (
            result_text == expected_result
        ), f"Ожидалось {expected_result}, получено {result_text}"
        print(f"✅ Результат верный: {result_text}")
