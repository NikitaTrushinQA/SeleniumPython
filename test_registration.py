from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings                                                   #для скрытия предупреждения
warnings.filterwarnings("ignore", category=DeprecationWarning)
import unittest
from selenium.webdriver.chrome.service import Service


class TestAbs(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        service = Service('D:\\Program Files (x86)\\PyCharm\\projects\\selenium_test1\\chromedriver.exe')
        browser = webdriver.Chrome(service=service)
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element("xpath", "//input[@class='form-control first' and @required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element("xpath", "//input[@class='form-control second' and @required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element("xpath", "//input[@class='form-control third' and @required]")
        input3.send_keys("Petrov@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text,'Congratulations! You have successfully registered!')

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        service = Service('D:\\Program Files (x86)\\PyCharm\\projects\\selenium_test1\\chromedriver.exe')
        browser = webdriver.Chrome(service=service)
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your first name']")
        first_name.send_keys('Petr')
        last_name = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your last name']")
        last_name.send_keys('Vasilev')
        email1 = browser.find_element(By.XPATH, "//input[@placeholder = 'Input your email']")
        email1.send_keys('V@gmail.com')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()






