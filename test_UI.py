#Если нужно проверить, что тест вызывает ожидаемое исключение (довольно редкая ситуация для UI-тестов,
# и вам этот способ, скорее всего, никогда не пригодится), мы можем использовать специальную конструкцию with pytest.raises().
# Например, можно проверить, что на странице сайта не должен отображаться какой-то элемент:

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()
#В первом тесте элемент будет найден, поэтому ошибка NoSuchElementException,
#которую ожидает контекстный менеджер pytest.raises, не возникнет, и тест упадёт.