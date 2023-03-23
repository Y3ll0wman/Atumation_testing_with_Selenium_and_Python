from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import unittest


def sel(link):
    browser = webdriver.Chrome()
    browser.get(link)

    elements = ["first_block input.form-control.first", "first_block input.form-control.second",
                "first_block input.form-control.third"]

    for element in elements:
        f_element = browser.find_element(By.CLASS_NAME, element)
        f_element.send_keys("fake_text")
    # Отправляем заполненную форму

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_element = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_element.text
    browser.quit()

    return welcome_text


class Test_welcome_text(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            sel(link),
            "Element h1 does not include text 'Congratulations! You have successfully registered!'"
        )

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            sel(link),
             "Element h1 does not include text 'Congratulations! You have successfully registered!'"
        )


if __name__ == '__main__':
    unittest.main()
