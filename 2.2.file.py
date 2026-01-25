import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    
    input1 = browser.find_element(By.NAME, value="firstname")
    input1.send_keys("Alise")
    input2 = browser.find_element(By.NAME, value="lastname")
    input2.send_keys("Mor")
    input3 = browser.find_element(By.NAME, value="email")
    input3.send_keys("qqq@qq.qq")

#Загрузить файл .txt. Он может быть пустым:

    # получаем путь к директории текущего исполняемого файла и отправляем файл
    file_input = browser.find_element(By.ID, "file")
    #r перед строкой - raw string (сырая/необработанная строка)
    file_input.send_keys(r'C:\chromedriver\file.txt')
    #print(f"Файл загружен: {'C:\chromedriver'}")

    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

finally:
    time.sleep(15)
    browser.quit()