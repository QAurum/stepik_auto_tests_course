#Вероятно, вы заметили, что мы не использовали в этом примере команду browser.quit(). Это привело к тому, что несколько окон браузера оставались открыты после окончания тестов, а закрылись только после завершения всех тестов. Закрытие браузеров произошло благодаря встроенной фикстуре — сборщику мусора. Но если бы количество тестов насчитывало больше нескольких десятков, то открытые окна браузеров могли привести к тому, что оперативная память закончилась бы очень быстро. Поэтому надо явно закрывать браузеры после каждого теста. Для этого мы можем воспользоваться финализаторами. Один из вариантов финализатора — использование ключевого слова Python: yield. После завершения теста, который вызывал фикстуру, выполнение фикстуры продолжится со строки, следующей за строкой со словом yield:
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://career.habr.com/"

@pytest.fixture

#Есть альтернативный способ вызова teardown кода с помощью встроенной фикстуры request и ее метода addfinalizer
#def fix_w_finalizer(request):
    #request.addfinalizer(partial(print, "finalizer_2"))
    #request.addfinalizer(partial(print, "finalizer_1"))
    
#def test_bar(fix_w_finalizers):
    #print("test_bar")

def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser #yield — это как "пауза" на время выполнения теста, а после теста выполняется очистка!
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit() #Закрывает все окна и вкладки браузера. Завершает процесс ChromeDriver. Освобождает память и ресурсы системы. Позволяет запустить новые тесты без конфликтов


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".button-comp--size-m").click()
        browser.find_element(By.CSS_SELECTOR, ".js-data-sign-in-btn")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".js-data-sign-in-btn")
