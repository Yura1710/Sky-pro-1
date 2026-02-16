import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=binary_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/classattr")
    print("Страница загружена")
    
    time.sleep(2)
    
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    print("Кнопка найдена")
    
    button.click()
    print("Клик выполнен!")
    
    time.sleep(3)
    
finally:
    driver.quit()
    print("Браузер закрыт")