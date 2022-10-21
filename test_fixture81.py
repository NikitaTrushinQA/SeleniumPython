import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import warnings                                                   #для скрытия предупреждения
import time
warnings.filterwarnings("ignore", category=DeprecationWarning)
link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    service = Service('D:\\Program Files (x86)\\PyCharm\\projects\\selenium_test1\\chromedriver.exe')
    browser = webdriver.Chrome(service=service)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


#Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И:
#pytest -s -v -m "smoke and win10" test_fixture81.py