
#Как работают методы get и find_element

#Тестовый сценарий выглядит так:

#1)Открыть страницу http://suninjuly.github.io/wait1.html
#2)Нажать на кнопку "Verify"
#3)Проверить, что появилась надпись "Verification was successful!"



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import warnings                                                   #для скрытия предупреждения
import time
warnings.filterwarnings("ignore", category=DeprecationWarning)

service = Service('D:\\Program Files (x86)\\PyCharm\\projects\\selenium_test1\\chromedriver.exe')
link= 'http://suninjuly.github.io/wait1.html'
browser = webdriver.Chrome(service=service)
browser.get(link)
time.sleep(1)

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text