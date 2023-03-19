import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script('button = document.getElementsByTagName("button")[0]; button.scrollIntoView(true);')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()