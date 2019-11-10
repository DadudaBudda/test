from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = " http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = (browser.find_element_by_id('num1')).text
    num2 = (browser.find_element_by_id('num2')).text
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_visible_text(str(int(num1) + int(num2)))
    button = browser.find_element_by_class_name("btn-default")
    button.click()
    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()
