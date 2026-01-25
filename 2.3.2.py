import os
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/redirect_accept.html"

try:
  browser = webdriver.Chrome()
  browser.get(link)
  time.sleep(1)

  button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
  button.click()

  browser.find_element(By.CSS_SELECTOR, value=".btn-primary").click()

  first_window = browser.window_handles[0]
  new_window = browser.window_handles[1]
  browser.switch_to.window(new_window)

  x_element = browser.find_element(By.ID, value="input_value")
  x = x_element.text

  def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  
  input1 = browser.find_element(By.ID, value="answer")
  input1.send_keys(calc(x))

  browser.find_element(By.CSS_SELECTOR, value=".btn-primary").click()

finally:
    time.sleep(15)
    browser.quit()
