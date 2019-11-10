import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = " http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = browser.find_element_by_id('num1')
    num1 = num1.text
    num2 = browser.find_element_by_id('num2')
    num2 = num2.text
    sum = str(int(num1) + int(num2))
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_visible_text(sum)
    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
