import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Рассчитать значение функции, которое нужно ввести в текстовое поле
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Считать значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # Посчитать математическую функцию от x
    y = calc(x)
    # Ввести ответ в текстовое поле
    input_answer_element = browser.find_element(By.ID, "answer")
    input_answer_element.send_keys(y)
    # Отметить checkbox "I'm the robot".
    check_box_element = browser.find_element(By.CSS_SELECTOR, ".form-check.form-check-custom .form-check-input")
    check_box_element.click()
    # Выбрать radiobutton "Robots rule!"
    radio_button_element = browser.find_element(By.CSS_SELECTOR, ".form-check.form-radio-custom .form-check-input")
    radio_button_element.click()
    # Нажать на кнопку Submit
    submit_button_element = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_button_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()