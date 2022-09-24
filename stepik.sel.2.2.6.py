#Задание на execute_script
#В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

#1)Открыть страницу http://SunInJuly.github.io/execute_script.html.
#2)Считать значение для переменной x.
#3)Посчитать математическую функцию от x.
#4)Проскроллить страницу вниз.
#5)Ввести ответ в текстовое поле.
#6)Выбрать checkbox "I'm the robot".
#7)Переключить radiobutton "Robots rule!".
#8)Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.chrome.service import Service
import warnings                                                   #для скрытия предупреждения
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    service = Service('D:\\Program Files (x86)\\PyCharm\\projects\\selenium_test1\\chromedriver.exe')
    link= 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    # cчитываем x
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    # передаем y в поле ответа
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    # отмечаем checkbox   "I'm the robot"
    robot_Checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_Checkbox.click()

    # выбираем radiobutton "Robots rule!"
    radiobutton_robots_rule = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton_robots_rule)
    radiobutton_robots_rule.click()

    # кликаем submit
    submit = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()