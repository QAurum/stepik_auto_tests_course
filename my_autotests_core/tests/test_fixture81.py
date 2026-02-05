import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()

class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login(self, browser):
        print(f"Открываю URL: {link}")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.Chrome
    def test_guest_should_see_basket_link_on_the_main_page(salf, browser):
        print(f"Открываю URL: {link}")
        browser.get(link)
        browser.save_screenshot("page_screenshot.png")
        print("Скриншот сохранен")
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-default.navbar-btn")

    # Чтобы пропустить тест, его отмечают в коде как:
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_guest_should_see_login_link(self, browser):
        print(f"Открываю URL: {link}")
        browser.get(link)
        browser.save_screenshot("page_screenshot.png")
        #print("Скриншот сохранен")
        browser.find_element(By.CSS_SELECTOR, "#login_link")
    # pytest -s -v -m "skip" test_fixture8.py
    # В результатах теста мы увидим "... 1 skipped" ....
    
    
    # помечать тест как ожидаемо падающий, чтобы о нем не забыть но и на результаты не влиял
    @pytest.mark.xfail(reason="fixing this bug right now") #pytest -rx -v test_fixture10a.py если резцльтат будет XPASS то это значит что тест неожиданно прошел (нарпимер,его починили)
    def test_guest_should_see_favorites_button_on_the_main_page(self, browser):
        print(f"Открываю URL: {link}")
        browser.get(link)
        browser.save_screenshot("page_screenshot.png")
        #print("Скриншот сохранен")
        browser.find_element(By.CSS_SELECTOR, ".input.btn.btn-default")


    #Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию. Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду:
    #pytest -s -v -m "not smoke" test_fixture8.py
    
    #Для запуска тестов с разными метками можно использовать логическое ИЛИ. Запустим smoke и regression-тесты:
    #pytest -s -v -m "smoke or regression" test_fixture8.py
    
    #Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И:
    #pytest -s -v -m "smoke and win10" test_fixture81.py
    
    
    #smoke or regression запускает тесты, которые имеют хотя бы одну из меток - smoke или regression.
    #smoke and regression запускает только те тесты, которые имеют две метки одновременно: и smoke, и regression.
