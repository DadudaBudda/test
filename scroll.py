from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"

try:
    browser.get(link)
    num1 = (browser.find_element_by_id('input_value')).text
    cal_element = browser.find_element_by_id('answer')
    cal_element.send_keys(calc(num1))
    robot = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    robot.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("arguments[0].scrollIntoView();", button)
    robot1 = browser.find_element_by_xpath('//input[@id="robotsRule"]')
    robot1.click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()