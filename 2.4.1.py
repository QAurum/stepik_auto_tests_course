import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд вместо time.sleep(1):
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait1.html")
    
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    #element_to_be_clickable вернет элемент, когда он станет кликабельным, иначе - False.
    button = WebDriverWait(browser, 5).until(                  #или until_not
            EC.element_to_be_clickable((By.ID, "verify"))
        )
    button.click()

    message = browser.find_element(By.ID, "verify_message") #ищем сообщение с эти ID
    assert "successful" in message.text #В этом сообщении должен быть текст "successful"

finally:
    time.sleep(10)
    browser.quit()