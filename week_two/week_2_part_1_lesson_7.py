import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Рассчитать значение функции, которое нужно ввести в текстовое поле
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Найти элемент-картинку, который является изображением сундука с сокровищами
    chest_element = browser.find_element(By.ID, "treasure")
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
    chest_element_attribute = chest_element.get_attribute("valuex")
    x = str(chest_element_attribute)
    # Посчитать математическую функцию от x
    y = calc(x)
    # Ввести ответ в текстовое поле
    input_answer_element = browser.find_element(By.ID, "answer")
    input_answer_element.send_keys(y)
    # Отметить checkbox "I'm the robot".
    check_box_element = browser.find_element(By.ID, "robotCheckbox")
    check_box_element.click()
    # Выбрать radiobutton "Robots rule!"
    radio_button_element = browser.find_element(By.ID, "robotsRule")
    radio_button_element.click()
    # Нажать на кнопку Submit
    submit_button_element = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_button_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()