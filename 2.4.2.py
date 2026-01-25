import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд вместо time.sleep(1):
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    #element_to_be_clickable вернет элемент, когда он станет кликабельным, иначе - False.

    WebDriverWait(browser, 12).until(   #можно не объявлять переменную если ее дальше не использовать
        EC.text_to_be_present_in_element((By.ID, 'price') ,'$100')
    )

    button = WebDriverWait(browser, 2).until(                  #или until_not
            EC.element_to_be_clickable((By.ID, "book"))
        )
    button.click()

    x_element = browser.find_element(By.ID, value="input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    browser.execute_script("window.scrollBy(0, 150);")

    input1 = browser.find_element(By.ID, value="answer")
    input1.send_keys(calc(x))

    button = browser.find_element(By.TAG_NAME, "button")
    #делает кнопку в области видимости еслио на перекрата:
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(10)
    browser.quit()