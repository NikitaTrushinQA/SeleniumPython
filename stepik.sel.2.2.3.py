from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.chrome.service import Service
import warnings                                                   #для скрытия предупреждения
from selenium.webdriver.support.ui import Select

def sum(x, y):
    return str(x + y)

try:
    service = Service('D:\\Program Files (x86)\\PyCharm\\projects\\selenium_test1\\chromedriver.exe')
    link= 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    # cчитываем x
    x_element = browser.find_element(By.ID, 'num1')
    x = int(x_element.text)

    # cчитываем y
    y_element= browser.find_element(By.ID, 'num2')
    y = int(y_element.text)
    # cчитываем сумму
    result = sum(x,y)
    #выбираем в dropdown значение
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(result)
    #кликаем submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()