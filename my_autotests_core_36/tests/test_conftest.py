import pytest
import selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.quit()

class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.Chrome
    def test_guest_should_see_basket_link_on_the_main_page(salf, browser):
        browser.get(link)
        browser.save_screenshot("page_screenshot.png")
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-default.navbar-btn")

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
    
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_favorites_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".input.btn.btn-default")
