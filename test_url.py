#Ваша задача — реализовать автотест со следующим сценарием действий:

#1)открыть страницу
#2)ввести правильный ответ
#3)нажать кнопку "Отправить"
#4)дождаться фидбека о том, что ответ правильный
#5)проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
#Правильным ответом на задачу в заданных шагах является число:
#answer = math.log(int(time.time()))
#Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров:
#https://stepik.org/lesson/236895/step/1
#https://stepik.org/lesson/236896/step/1
#https://stepik.org/lesson/236897/step/1
#https://stepik.org/lesson/236898/step/1
#https://stepik.org/lesson/236899/step/1
#https://stepik.org/lesson/236903/step/1
#https://stepik.org/lesson/236904/step/1
#https://stepik.org/lesson/236905/step/1
#В упавших тестах найдите кусочки послания. Тест должен падать,
#если текст в опциональном фидбеке не совпадает со строкой "Correct!"
#Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.
import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('endpoint', [236895,236896,236897,236898,236899,236903,236904,236905])
def test_urls(browser,endpoint):
    link = f"https://stepik.org/lesson/{endpoint}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    answer_field = browser.find_element(By.CLASS_NAME, 'ember-text-area.ember-view.textarea.string-quiz__textarea')
    #задаем переменную,в которую собираем кусочки текста в одно предложение
    global message
    answer = math.log(int(time.time()))
    answer_field.send_keys(answer)

    submit = browser.find_element(By.CLASS_NAME,'submit-submission')
    submit.click()
    browser.implicitly_wait(10)
    #проверяем совпадение текста в опциональном фидбеке
    text1 = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
    ect_text = text1.text

    try:
        assert ect_text == "Correct!"
    except AssertionError:
        message += ect_text



if __name__ == "__main__":
    pytest.main()
