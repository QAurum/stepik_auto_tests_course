from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")
elements = browser.find_elements(By.TAG_NAME, value="input")
for element in elements:
    element.send_keys("Ответ")

button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
button.click()

time.sleep(30)
browser.quit()
