import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=binary_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    print("Страница Dynamic ID загружена")
    
    time.sleep(2)
    
    button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
    print("Кнопка найдена по тексту")
    
    button.click()
    print("Клик выполнен!")
    
    time.sleep(3)
    
finally:
    driver.quit()
    print("Браузер закрыт")