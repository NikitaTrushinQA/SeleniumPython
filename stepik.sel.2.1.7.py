#Задание: поиск сокровища с помощью get_attribute
#Ваша программа должна:

#1)Открыть страницу http://suninjuly.github.io/get_attribute.html.
#2)Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
#3)Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
#4)Посчитать математическую функцию от x (сама функция остаётся неизменной).
#5)Ввести ответ в текстовое поле.
#6)Отметить checkbox "I'm the robot".
#7)Выбрать radiobutton "Robots rule!".
#8)Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.chrome.service import Service
import warnings                                                   #для скрытия предупреждения
warnings.filterwarnings("ignore", category=DeprecationWarning)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    service = Service('D:\\Program Files (x86)\\PyCharm\\projects\\selenium_test1\\chromedriver.exe')
    link= 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome(service=service)
    browser.get(link)
    
    # cчитываем x
    chest = browser.find_element(By.ID, "treasure")
    chest_value = chest.get_attribute("valuex")
    x = chest_value
    y = calc(x)

    # передаем y в поле ответа
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