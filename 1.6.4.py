from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.TAG_NAME, value="input")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, value="last_name")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CLASS_NAME, value="form-control.city")
input3.send_keys("Smolensk")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")
button = browser.find_element(By.XPATH, '//button [text()="Submit"]')
button.click()

time.sleep(30)
browser.quit()
