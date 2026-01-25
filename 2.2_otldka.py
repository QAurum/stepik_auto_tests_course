#А, понятно! Ты запускаешь код построчно в интерактивной консоли Python, и там проблемы с отступами!
#Нельзя запускать код с блоками try/except/finally построчно в интерактивном режиме. Нужно:
#Запускать весь скрипт сразу
#Или использовать Jupyter Notebook
#Или писать в файле и запускать его
#типо python test.py




#Вместо встроенных find_element_by... можно использовать вот такую конструкцию:
#element = browser.execute_script('document.getElementsByName("name")')

#Так же есть конструкции:
#getElementById
#getElementsByTagName
#getElementsByClassName
#querySelector - для CSS
#querySelectorAll - для CSS (находит все совпадения)
#evaluate - для XPATH.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

print("=== Запуск теста ===")
browser = webdriver.Chrome()

try:
    print("Шаг 1: Открываю страницу...")
    browser.get(link)
    
    # Простая пауза для загрузки
    time.sleep(3)
    
    print(f"Шаг 2: Страница загружена. Title: {browser.title}")
    print(f"Шаг 3: Current URL: {browser.current_url}")
    
    # Проверим, что вообще на странице
    print(f"Шаг 4: Всего элементов на странице: {len(browser.find_elements(By.XPATH, '//*'))}")
    
    print("Шаг 5: Заполняю форму...")
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    
    print("Шаг 6: Нажимаю кнопку...")
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()
    
    print("Шаг 7: Жду результат...")
    time.sleep(5)
    
    # Проверяем alert
    alert = browser.switch_to.alert
    print(f"Шаг 8: Alert текст: {alert.text}")
    alert.accept()
    
    print("=== Тест пройден успешно! ===")
    # Скриншот для проверки
    browser.save_screenshot("screen_win.png")
    
except Exception as e:
    print(f"=== ОШИБКА: {type(e).__name__} ===")
    print(f"Сообщение: {e}")
    import traceback
    traceback.print_exc()
    # Скриншот для проверки
    browser.save_screenshot("screen_error.png")
    
finally:
    print("Шаг 9: Закрываю браузер...")
    browser.quit()