#Задание: переход на новую вкладку
#В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

#Сценарий для реализации выглядит так:

#1)Открыть страницу http://suninjuly.github.io/redirect_accept.html
#2)Нажать на кнопку
#3)Переключиться на новую вкладку
#4)Пройти капчу для робота и получить число-ответ



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
    link= 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome(service=service)
    browser.get(link)
    #нажимаем кнопку
    button = browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary')
    button.click()
    #переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # cчитываем x
    x_element = browser.find_element(By.ID, 'input_value')
    x = int(x_element.text)
    result = calc(x)
    # заполняем поле с ответом
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(result)
    # кликаем кнопку
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()