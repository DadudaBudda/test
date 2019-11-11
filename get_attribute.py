import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    people_radio = browser.find_element_by_id("treasure")
    people_checked = people_radio.get_attribute("valuex")
    cal_element = browser.find_element_by_id('answer')
    cal_element.send_keys(calc(people_checked))
    robot = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
    robot.click()
    robot1 = browser.find_element_by_xpath('//input[@id="robotsRule"]')
    robot1.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
