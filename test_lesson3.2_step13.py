# оформление примера lesson1_6_step_10 с использованием тест-ранера unittest

from selenium imp ort webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):

        link = "http://suninjuly.github.io/registration1.html"  # рабочая ссылка
        browser = webdriver.Chrome()
        browser.get(link)

        #код, который заполняет обязательные поля

        input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div/input[@class="form-control first"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div/input[@class="form-control second"]')
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div/input[@class="form-control third"]')
        input3.send_keys("Ivan@YA.RU")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # self.assertEqual('что должно быть', 'что есть', 'что произошло')
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "что-то произошло в тесте1")
        time.sleep(10)
          # закрываем браузер после всех манипуляций
        browser.quit()

    def test_abs2(self):

        link = "http://suninjuly.github.io/registration2.html" #нерабочая ссылка
        browser = webdriver.Chrome()
        browser.get(link)

        #код, который заполняет обязательные поля

        input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div/input[@class="form-control first"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div/input[@class="form-control second"]')
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div/input[@class="form-control third"]')
        input3.send_keys("Ivan@YA.RU")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # self.assertEqual('что должно быть', 'что есть', 'что произошло')
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "что-то произошло в тесте2")

if __name__ == "__main__":
    unittest.main()