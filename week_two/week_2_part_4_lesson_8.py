import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # формула для вычисления ответа капчи
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.ID, 'price'), '$100')
    )
    # Нажать на кнопку "Book"
    button = browser.find_element(By.ID, 'book').click()
    # Решить уже известную нам математическую задачу
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    input_answer_element = browser.find_element(By.ID, 'answer')
    input_answer_element.send_keys(y)
    # Нажать на кнопку Submit
    browser.find_element(By.ID, 'solve').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()