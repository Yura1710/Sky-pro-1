from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

service = Service(executable_path=binary_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    print("Страница загружена, ожидаем загрузки 3-х изображений...")
    
    wait = WebDriverWait(driver, 20)
    wait.until(
        lambda driver: len(driver.find_elements(By.TAG_NAME, "img")) >= 3
    )
    
    images = driver.find_elements(By.TAG_NAME, "img")
    print(f"Найдено изображений: {len(images)}")
    
    if len(images) >= 3:
        third_image = images[2]
        src_value = third_image.get_attribute("src")
        
        print("\n" + "="*50)
        print("Атрибут src у 3-й картинки:")
        print(src_value)
        print("="*50 + "\n")
    else:
        print("Не удалось загрузить 3 изображения")
    
finally:
    driver.quit()
    print("Браузер закрыт")