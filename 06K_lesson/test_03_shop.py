from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestShop:
    """Тесты для интернет-магазина"""

    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def teardown_method(self):
        if self.driver:
            self.driver.quit()

    def test_example(self):
        self.driver.get("https://example.com")
        assert "Example" in self.driver.title
        print("✅ Тест-заглушка работает")
