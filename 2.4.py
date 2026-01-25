import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд вместо time.sleep(1):
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait1.html")
    
    button = browser.find_element(By.ID, "verify").click()
    message = browser.find_element(By.ID, "verify_message") #ищем сообщение с эти ID
    assert "successful" in message.text #В этом сообщении должен быть текст "successful"

finally:
    time.sleep(10)
    #browser.quit()
