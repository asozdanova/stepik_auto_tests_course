from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import math
import time

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'file.txt')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    #time.sleep(30)  # добавить эту строку после запуска браузера
    browser.get(link)

# Ваш код, который заполняет поля
    input1 = browser.find_element(By.CSS_SELECTOR, '.form-control[name="firstname"]')
    input1.send_keys('Ivan')
    input2 = browser.find_element(By.CSS_SELECTOR, '.form-control[name="lastname"]')
    input2.send_keys('Petrov')
    input3 = browser.find_element(By.CSS_SELECTOR, '.form-control[name="email"]')
    input3.send_keys('a@email')
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

# Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
