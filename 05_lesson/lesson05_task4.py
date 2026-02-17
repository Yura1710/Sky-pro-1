import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/login")
    print("Страница логина загружена")
    time.sleep(2)
    
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")
    print("Логин введён")
    time.sleep(1)
    
    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")
    print("Пароль введён")
    time.sleep(1)
    
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()
    print("Кнопка Login нажата")
    time.sleep(2)
    
    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    message_text = success_message.text
    print("\n" + "="*50)
    print("СООБЩЕНИЕ ПОСЛЕ ВХОДА:")
    print("="*50)
    print(message_text)
    print("="*50 + "\n")
    
    time.sleep(3)
    
finally:
    driver.quit()
    print("Браузер закрыт")
