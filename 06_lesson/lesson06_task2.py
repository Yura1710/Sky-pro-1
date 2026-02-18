from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

service = Service(executable_path=binary_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/textinput")
    print("Страница загружена")

    input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
    input_field.send_keys("SkyPro")
    print("Текст 'SkyPro' введён")

    button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    button.click()
    print("Кнопка нажата")

    wait = WebDriverWait(driver, 5)
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
    )

    button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
    print("\n" + "="*50)
    print("Текст кнопки после изменения:")
    print(button_text)
    print("="*50 + "\n")

finally:
    driver.quit()
    print("Браузер закрыт")

