import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test323(unittest.TestCase):

    
    def setUp(self):
        #Выполняется перед КАЖДЫМ тестом"""
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)  # неявное ожидание
    
    def tearDown(self):
        #Выполняется после КАЖДОГО теста"""
        self.browser.quit()
    
    def test_323_1(self):
        #Тест для первой страницы (должен пройти успешно)"""
        self.browser.get("http://suninjuly.github.io/registration1.html")
        
        # Заполняем поля (как в test_3_2_31.py)
        self.browser.find_element(By.CLASS_NAME, "first").send_keys("Ivan")
        self.browser.find_element(By.CLASS_NAME, "second").send_keys("Petrov")
        self.browser.find_element(By.CLASS_NAME, "third").send_keys("testtesttest@gmaill.com")
        
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        
        time.sleep(5)
        
        # Проверяем результат (вместо assert используем assertEqual)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!",
            f"Ожидался текст 'Congratulations! You have successfully registered!', "
            f"а получен '{welcome_text}'"
        )
    
    
    
    def test_323_2(self):
        #"""Тест для второй страницы (должен упасть с NoSuchElementException)"""
        self.browser.get("http://suninjuly.github.io/registration2.html")
        
        # Первое поле (должно найтись)
        self.browser.find_element(By.CLASS_NAME, "first").send_keys("Ivan")
        
        # ВТОРОЕ ПОЛЕ - вот здесь будет ошибка NoSuchElementException!
        # На второй странице нет поля с классом "second" внутри .first_block
        self.browser.find_element(By.CLASS_NAME, ".input.second").send_keys("Petrov")
        
        # Третье поле
        self.browser.find_element(By.CLASS_NAME, "third").send_keys("testtesttest@gmaill.com")
        
        # Кнопка
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        
        # Этот код не выполнится, если выше была ошибка
        time.sleep(1)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()
