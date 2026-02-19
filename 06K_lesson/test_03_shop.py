from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestShop:
    """Тесты для интернет-магазина"""

    def setup_method(self):
        """Настройка браузера перед тестом"""
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def teardown_method(self):
        """Закрытие браузера после теста"""
        if self.driver:
            self.driver.quit()

    def test_example(self):
        """Пример теста (замени на реальный)"""
        self.driver.get("https://example.com")
        assert "Example" in self.driver.title
        print("✅ Тест-заглушка работает")
