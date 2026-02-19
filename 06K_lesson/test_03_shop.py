import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestShop:
    """Тесты для интернет-магазина"""

    def setup_method(self):
        """Настройка браузера перед каждым тестом"""
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        """Закрытие браузера после теста"""
        if self.driver:
            self.driver.quit()

    def test_example(self):
        """Пример теста (замени на реальный)"""
        self.driver.get("https://example.com")
        assert "Example" in self.driver.title
        print("✅ Тест-заглушка работает")