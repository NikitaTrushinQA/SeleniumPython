from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings                                                   #для скрытия предупреждения
warnings.filterwarnings("ignore", category=DeprecationWarning)
try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome(executable_path=r'D:\Program Files (x86)\PyCharm\projects\selenium_test1\chromedriver.exe')
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Nikita")
    input2 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div[1]/div[2]/input')
    input2.send_keys("Trushin")
    input3 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[3]/input")
    input3.send_keys("nikitatrushinqa@gmail.com")

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
    assert "Сongratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()