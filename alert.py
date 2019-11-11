import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    button = browser.find_element_by_class_name("btn-primary")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    cal_element = browser.find_element_by_id('answer')
    cal_element.send_keys(calc(x))
    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn-primary")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
