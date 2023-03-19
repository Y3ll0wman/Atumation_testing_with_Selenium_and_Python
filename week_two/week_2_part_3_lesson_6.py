import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # формула для вычисления ответа капчи
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    # Нажать на кнопку
    browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary').click()
    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # Пройти капчу для робота и получить число-ответ
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    input_answer_element = browser.find_element(By.ID, 'answer')
    input_answer_element.send_keys(y)
    # Нажать на кнопку Submit
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()