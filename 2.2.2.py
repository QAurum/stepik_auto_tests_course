import math
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(1)

try:
  x_element = browser.find_element(By.ID, value="num1")
  x = x_element.text
  #print(x)
  y_element = browser.find_element(By.ID, value="num2")
  y = y_element.text
  #print(y)
  z = int(x)+int(y)   #вычисляю как число
  z = str(z)    #превращаю наад в строку
  #print(f"Сумма как строка: {z}")
  
  dropdown = browser.find_element(By.ID, "dropdown")
  browser.find_element(By.ID, "dropdown").click()
  select = Select(dropdown)

  #select.select_by_value(z)  # ищем <option value="579">579</option>
  # или так: 
  #select.select_by_value(z) # ищем элемент с текстом = z
  select.select_by_visible_text(z)

  button = browser.find_element(By.TAG_NAME, "button")
  #делает кнопку в области видимости еслио на перекрата:
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  browser.find_element(By.CSS_SELECTOR, value=".btn-default").click()

finally:
    time.sleep(5)
    browser.quit()