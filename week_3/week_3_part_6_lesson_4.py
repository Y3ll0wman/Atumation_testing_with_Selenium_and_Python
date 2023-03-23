import pytest
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestLogin:
    def test_login_in_stepik(self, browser, login, password):
        link = f"https://stepik.org/lesson/236895/step/1"
        browser.get(link)

        button_login = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "ember33"))
        )

        button_login.click()
        email_input = browser.find_element(By.ID, "id_login_email")
        email_input.send_keys(login)
        password_input = browser.find_element(By.ID, "id_login_password")
        password_input.send_keys(password)
        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader").click()

        text_area = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "ember33"))
        )

        # text_area = browser.find_element(By.ID, "ember85")

        text_area.send_keys("Hello World!")
        browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
        time.sleep(10)
