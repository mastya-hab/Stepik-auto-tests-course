import time
from selenium import webdriver

browser=webdriver.Chrome()

time.sleep(5)

browser.get("http://suninjuly.github.io/simple_form_find_task.html")

input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
    
#input1 = browser.find_element_by_tag_name(input)
#input1.send_keys("Ivan")
#time.sleep(5)
#input1 = browser.find_element_by_tag_name(input)
#input1.send_keys("Ivan")

 
