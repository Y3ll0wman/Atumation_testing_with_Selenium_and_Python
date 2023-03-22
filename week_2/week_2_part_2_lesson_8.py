import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    first_name_element = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    first_name_element.send_keys("Konstantin")
    last_name_element = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    last_name_element.send_keys("Varvarkin")
    email_name_element = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email_name_element.send_keys("Konstantin@mail.com")
    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    # Получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    # Отправляем файл
    file_element = browser.find_element(By.ID, "file")
    file_element.send_keys(file_path)
    # Нажать кнопку "Submit"
    submit_button_element = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit_button_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()