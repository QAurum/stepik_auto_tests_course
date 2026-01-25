import math
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


link = "https://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(1)
link = browser.find_element(By.LINK_TEXT, value=str(math.ceil(math.pow(math.pi, math.e)*10000)))

try:
  link.click()

  imgX = browser.find_element(By.ID, "treasure")
  x = imgX.get_attribute("valuex")
  def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

  input1 = browser.find_element(By.ID, value="answer")
  input1.send_keys(calc(x))

  option1 = browser.find_element(By.ID, value="robotCheckbox")
  option1.click()
  option2 = browser.find_element(By.ID, value="robotsRule")
  option2.click()

  button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-default")))
  button.click()

finally:
    time.sleep(5)
    browser.quit()