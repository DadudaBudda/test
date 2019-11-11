import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(12)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser.get("http://suninjuly.github.io/explicit_wait2.html")
try:
    price = WebDriverWait(browser, 12).until(EC. text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element_by_id("book")
    button.click()
    button1 = browser.find_element_by_id("solve")
    browser.execute_script("arguments[0].scrollIntoView();", button1)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    cal_element = browser.find_element_by_id('answer')
    cal_element.send_keys(calc(x))
    button1 = browser.find_element_by_id("solve")
    button1.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
