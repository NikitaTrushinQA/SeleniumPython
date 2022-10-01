#Задание: ждем нужный текст на странице
#Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
# Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

#В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

#1)Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#2)Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
#3)Нажать на кнопку "Book"
#4)Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import warnings                                                   #для скрытия предупреждения
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
warnings.filterwarnings("ignore", category=DeprecationWarning)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    service = Service('D:\\Program Files (x86)\\PyCharm\\projects\\selenium_test1\\chromedriver.exe')
    link= 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome(service=service)
    browser.get(link)
    # говорим Selenium Дождаться, когда цена дома уменьшится до $100 (ожидание не меньше 12сек)
    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),'$100')
        )

    btn = browser.find_element(By.ID, 'book')
    btn.click()

    #решаем математическую задачу
    x_element = browser.find_element(By.ID, 'input_value')
    x = int(x_element.text)
    result = calc(x)
    # заполняем поле с ответом
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(result)
    # кликаем кнопку
    button_submit = browser.find_element(By.ID, 'solve')
    button_submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()