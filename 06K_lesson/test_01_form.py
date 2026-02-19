from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import os


class TestForm:
    """Тесты для проверки формы data-types"""

    def setup_method(self):
        """Настройка браузера перед каждым тестом"""
        driver_path = os.path.join(os.getcwd(), "msedgedriver.exe")
        if not os.path.exists(driver_path):
            raise FileNotFoundError(
                f"Драйвер не найден по пути: {driver_path}\n"
                "Скачай его с https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/"
            )
        service = Service(driver_path)
        self.driver = webdriver.Edge(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        """Закрытие браузера после теста"""
        if self.driver:
            self.driver.quit()

    def test_form_validation(self):
        """Тест проверки формы"""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
        }
        for field_id, value in fields.items():
            element = self.driver.find_element(By.NAME, field_id)
            element.clear()
            element.send_keys(value)
        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        submit_button.click()
        self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".alert-success, .alert-danger")
            )
        )
        zip_code_field = self.driver.find_element(By.ID, "zip-code")
        zip_code_class = zip_code_field.get_attribute("class")
        assert "alert-danger" in zip_code_class, \
            f"Zip code должен быть красным, но класс: {zip_code_class}"
        print("✅ Поле Zip code красное (верно)")
        fields_to_check = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company",
        ]
        for field_id in fields_to_check:
            field = self.driver.find_element(By.ID, field_id)
            field_class = field.get_attribute("class")
            assert (
                "alert-success" in field_class
            ), f"Поле {field_id} должно быть зелёным"
            print(f"✅ Поле {field_id} зелёное")
        print("🎉 Все проверки пройдены успешно!")
