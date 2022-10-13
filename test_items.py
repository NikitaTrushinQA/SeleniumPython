
import time
from selenium.webdriver.common.by import By
def test_check_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    try:
        button = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket").is_enabled()
        assert button, "Кнопка 'Добавить в корзину' не найдена"
    finally:
        time.sleep(5)
