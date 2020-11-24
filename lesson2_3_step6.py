from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

# Открыть страницу
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_window = browser.window_handles[0]  # запоминаем имя текущей вкладки
    print("first_window: ", first_window)
    time.sleep(3)

# Нажать на кнопку
    button = browser.find_element_by_tag_name("button")
    button.click()

# Переключиться на новую вкадку

    new_window = browser.window_handles[1]  # запоминаем имя новой вкладки
    print("new_window: ", new_window)
    window_name = new_window

    browser.switch_to.window(window_name) # переходим в новую вкладку


# На новой странице решить капчу для роботов
    x1 = browser.find_element_by_id("input_value")
    x = x1.text
    y = calc(x)

    print("x: ", x)
    print("y: ", y)

# Вводим ответ в поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

# Нажимае на кноку Submit
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