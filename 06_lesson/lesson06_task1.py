from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

service = Service(executable_path=binary_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/ajax")
    print("Страница загружена")
    
    button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
    button.click()
    print("Кнопка нажата")
    
    wait = WebDriverWait(driver, 20)
    success_message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )
    
    message_text = success_message.text
    print("\n" + "="*50)
    print("Текст из зелёной плашки:")
    print(message_text)
    print("="*50 + "\n")
    
    expected_text = "Data loaded with AJAX get request."
    if message_text == expected_text:
        print("✅ Текст соответствует ожидаемому")
    else:
        print(f"❌ Текст не соответствует. Ожидалось: '{expected_text}'")
    
finally:
    driver.quit()
    print("Браузер закрыт")
