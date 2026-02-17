import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    print("Страница загружена")
    time.sleep(2)
    input_field = driver.find_element(By.TAG_NAME, "input")
    print("Поле ввода найдено")
    input_field.send_keys("Sky")
    print("Введено: Sky")
    time.sleep(2)
    input_field.clear()
    print("Поле очищено")
    time.sleep(2)
    input_field.send_keys("Pro")
    print("Введено: Pro")
    time.sleep(2)
finally:
    driver.quit()
    print("Браузер закрыт")
