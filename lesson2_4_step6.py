from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока price = $100
    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )

    button = browser.find_element_by_id("book")
    button.click()

# решаем капчу для роботов
    x1 = browser.find_element_by_id("input_value")
    x = x1.text
    y = calc(x)

    print("x: ", x)
    print("y: ", y)

# Вводим ответ в поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

# Нажимае на кноку Submit
    button2 = browser.find_element_by_id("solve")
    button2.click()

# Переходим в модальное окно, копирум текст выводим его
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept() # Нажимаем ОК в модальном окне

finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
# закрываем браузер после всех манипуляций
    browser.quit()