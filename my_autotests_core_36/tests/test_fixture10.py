import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

#@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])

# Параметризация ссылок
links = [
    "https://stepik.org/lesson/236895/step/1"#,
    #"https://stepik.org/lesson/236896/step/1",
    #"https://stepik.org/lesson/236897/step/1",
    #"https://stepik.org/lesson/236898/step/1",
    #"https://stepik.org/lesson/236899/step/1",
    #"https://stepik.org/lesson/236903/step/1",
    #"https://stepik.org/lesson/236904/step/1",
    #"https://stepik.org/lesson/236905/step/1"
]
@pytest.mark.parametrize('link', links)
def test_gest_should_log_in(browser, link):
# ОЧИСТИТЬ КУКИ ПЕРЕД ТЕСТОМ
    browser.delete_all_cookies()
    print("/nCookies очищены")
    browser.refresh()
    time.sleep(5)
    wait = WebDriverWait(browser, 10)
    print(f"\nТестируем страницу: {link}")
    browser.get(link)
    
    time.sleep(3)
    button_enter = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login")
    button_enter.click() #button "Войти"
    print("\nВОЙТИ")
    time.sleep(2)
    
    print("\nВВЕДЕМ ЗНАЧЕНИЯ...")
    #modal_content = wait.until(
    #        EC.presence_of_element_located((By.ID, "modal-dialog__content"))
    #    )


#    modal_elements = browser.find_elements(By.CSS_SELECTOR, "[id*='modal'], [id*='dialog']")
#    print(f"   По ID найдено: {len(modal_elements)}")
#    for elem in modal_elements:
#        print(f"     ID: {elem.get_attribute('id')}")
#    
#    # По классу
#    class_elements = browser.find_elements(By.CSS_SELECTOR, "[class*='modal'], [class*='dialog']")
#    print(f"   По классу найдено: {len(class_elements)}")
#    for elem in class_elements[:3]:  # первые 3
#        print(f"     Класс: {elem.get_attribute('class')}")
        


    email_field = browser.find_element(By.NAME, "login")
    print("\nFIND EMAIL")
    email_field.send_keys("aurumkes@yandex.ru")
    print("\nPASS EMAIL")
    password_field = browser.find_element(By.NAME, "password")
    print("\nFIND PASSWORW")
    password_field.send_keys("Sirano042")
    print("\nPASS PASSWORD")
    button_green = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    button_green.click()
    #browser.refresh()
    time.sleep(15)
    
    print("\nИЩЕМ ПОЛЕ")
    input_textarea = browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")
    
    #print("\nждем пока станет кликабельным")
    #input_textarea = WebDriverWait(browser, 15).until(
    #EC.element_to_be_clickable((By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea"))
    #)
    #print("\nПоле стало кликабельным")

    input_textarea.click() # Кликаем в поле
    time.sleep(0.5)
    
    print("\nЧИСТИМ ПОЛЕ")
    input_textarea.clear()  # очищает поле
    
    print("\nЖДЕМ НЕМНОГО И ВВОДИМ РАСЧЕТНОЕ ЗНАЧЕНИЕ")
    time.sleep(0.5)
    answer = str(math.log(int(time.time())))
    input_textarea.send_keys(answer) #изначально answer - число, а send_keys ожидает строку, поэтому пишем через f или нужно преобразование answer = str(math.log(int(time.time())))
    print("\nОТПРАВИТЬ")
    button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    button.click()
    time.sleep(5)
    
    print("\nФИТБЭК")
    message = browser.find_element(By.CLASS_NAME, ".smart-hints__hint") #ищем сообщение с эти ID
    assert "Correct" in message.text #В этом сообщении должен быть текст "successful"
    
    #if feedback.is_displayed():
        #print("\nЭлемент виден на странице")
    #else:
        #print("\nЭлемент скрыт (display: none, visibility: hidden и т.д.)")
    print("\проверить, что текст в фидбеке имеет Correct!")
