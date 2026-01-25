import os
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/alert_accept.html"

try:
  browser = webdriver.Chrome()
  browser.get(link)
  time.sleep(1)

  button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
  button.click()

   #Узнаем имя ново вкладки методом window_handles
   #Он возвращает массив имён всех вкладок
   #Зная что открыто всего две вкладки - выбираем вторую вкладку:
  new_window = browser.window_handles[1]

  #Мы можем запомнить имя текущей вкладки, чтобы потом к ней вернуться:
  first_window = browser.window_handles[0]

  #Для переключения на новую вкладку надо явно указать,
  #куда перейти с помощью команды switch_to.window:
  browser.switch_to.window(new_window)

  browser.find_element(By.CSS_SELECTOR, value=".btn-primary").click()

finally:
    time.sleep(15)
    browser.quit()
