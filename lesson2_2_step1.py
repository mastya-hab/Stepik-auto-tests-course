from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element_by_id("num1")
    y1 = browser.find_element_by_id("num2")

    x = x1.text
    y = y1.text
    z = str(int(x) + int(y))

    print("x: ", x)
    print("y: ", y)
    print("z: ", z)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z) # ищем элемент с текстом "z"

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()