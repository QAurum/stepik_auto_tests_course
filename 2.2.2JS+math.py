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
  x_element = browser.find_element(By.ID, value="input_value")
  x = x_element.text

  def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  #print(x)
  
  #проскроллить страницу вниз
  browser.execute_script("window.scrollBy(0, 50);")
  
  input1 = browser.find_element(By.ID, value="answer")
  input1.send_keys(calc(x))

  option1 = browser.find_element(By.ID, value="robotCheckbox")
  option1.click()
  option2 = browser.find_element(By.ID, value="robotsRule")
  option2.click()

  button = browser.find_element(By.TAG_NAME, "button")
  #делает кнопку в области видимости еслио на перекрата:
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  browser.find_element(By.CSS_SELECTOR, value=".btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()