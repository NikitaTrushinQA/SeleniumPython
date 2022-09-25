#Задание: загрузка файла
#В этом задании в форме регистрации требуется загрузить текстовый файл.

#Напишите скрипт, который будет выполнять следующий сценарий:

#1)Открыть страницу http://suninjuly.github.io/file_input.html
#2)Заполнить текстовые поля: имя, фамилия, email
#3)Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#4)Нажать кнопку "Submit"
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.chrome.service import Service
import warnings                                                   #для скрытия предупреждения
from selenium.webdriver.support.ui import Select
warnings.filterwarnings("ignore", category=DeprecationWarning)
try:
    service = Service('D:\\Program Files (x86)\\PyCharm\\projects\\selenium_test1\\chromedriver.exe')
    link= 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//input[@placeholder = 'Enter first name']")
    input1.send_keys("Nikita")
    input2 = browser.find_element(By.XPATH, "//input[@placeholder = 'Enter last name']")
    input2.send_keys("Trushin")
    input3 = browser.find_element(By.XPATH, "//input[@placeholder ='Enter email']")
    input3.send_keys("nikitatrushinqa@gmail.com")

    #загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)          # добавляем к этому пути имя файла
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    # кликаем submit
    submit = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()