#Ваша программа должна выполнить следующие шаги:

#Открыть страницу https://suninjuly.github.io/math.html.
#Считать значение для переменной x.
#Посчитать математическую функцию от x (код для этого приведён ниже).
#Ввести ответ в текстовое поле.
#Отметить checkbox "I'm the robot".
#Выбрать radiobutton "Robots rule!".
#Нажать на кнопку Submit.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.chrome.service import Service

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    service = Service('D:\\Program Files (x86)\\PyCharm\\projects\\selenium_test1\\chromedriver.exe')
    link= 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    #cчитываем x
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    #передаем y в поле ответа
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    # отмечаем checkbox   "I'm the robot"
    robot_Checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_Checkbox.click()

    #выбираем radiobutton "Robots rule!"
    radiobutton_robots_rule = browser.find_element(By.CSS_SELECTOR,'[value="robots"]')
    radiobutton_robots_rule.click()
    #кликаем submit
    submit = browser.find_element(By.CLASS_NAME,'btn.btn-default')
    submit.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()