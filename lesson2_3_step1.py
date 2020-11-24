from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

# Открыть страницу
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_window = browser.window_handles[0]  # запоминаем имя текущей вкладки
    print("first_window: ", first_window)

# Нажать на кнопку
    button = browser.find_element_by_tag_name("button")
    button.click()
# Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()
# На новой странице решить капчу для роботов
    x1 = browser.find_element_by_id("input_value")
    x = x1.text
    y = calc(x)

    print("x: ", x)
    print("y: ", y)
# Вводим ответ в поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

# Нажимае на ктивированную кноку
    button = browser.find_element_by_tag_name("button")
    button.click()
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