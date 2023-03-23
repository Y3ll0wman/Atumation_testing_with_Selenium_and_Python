import pytest
import time
import math

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1",
                                 "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1",
                                 "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1",
                                 "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1",
                                 "https://stepik.org/lesson/236905/step/1"])
class TestLogin:
    def test_ufo_in_stepik(self, browser, login, password, url):
        link = url
        answer = math.log(int(time.time()))
        # открыть страницу
        browser.get(link)
        # авторизоваться на странице со своим логином и паролем
        button_login = WebDriverWait(browser, 60).until(
            EC.element_to_be_clickable((By.ID, "ember33"))
        )
        button_login.click()
        email_input = browser.find_element(By.ID, "id_login_email")
        email_input.send_keys(login)
        password_input = browser.find_element(By.ID, "id_login_password")
        password_input.send_keys(password)
        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader").click()
        time.sleep(2)
        # ввести правильный ответ
        text_area = WebDriverWait(browser, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea"))
        )
        text_area.send_keys(answer)
        time.sleep(2)
        # нажать на кнопку "Отправить"
        button_submit = WebDriverWait(browser, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        button_submit.click()
        time.sleep(3)
        # проверить, что текст в фидбеке полностью совпадает с "Correct!"
        feedback_text_element = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
        #time.sleep(3)
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        feedback_text = feedback_text_element.text
        #time.sleep(3)
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

        assert "Correct!" in feedback_text
        time.sleep(3)
