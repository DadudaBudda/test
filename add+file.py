from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)
    fname = browser.find_element_by_name('firstname')
    fname.send_keys('Maxim')
    lname = browser.find_element_by_name('lastname')
    lname.send_keys('privet')
    mail = browser.find_element_by_name('email')
    mail.send_keys('privet')
    element = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)
    button = browser.find_element_by_class_name("btn-primary")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
