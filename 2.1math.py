import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

#обновление версии вебдрайвера
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#service = Service(ChromeDriverManager().install())
#browser = webdriver.Chrome(service=service)

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

link = browser.find_element(By.LINK_TEXT, value=str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()

x_element = browser.find_element(By.ID, value="input_value")
x = x_element.text
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


input1 = browser.find_element(By.ID, value="answer")
input1.send_keys(calc(x))

option1 = browser.find_element(By.ID, value="robotCheckbox")
option1.click()
option2 = browser.find_element(By.ID, value="robotsRule")
option2.click()

button = browser.find_element(By.CSS_SELECTOR, value="btn.btn-default")
button.click()