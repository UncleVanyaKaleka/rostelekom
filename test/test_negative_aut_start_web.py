import time
import pytest
import chromedriver_autoinstaller
import Data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wdw
chromedriver_autoinstaller.install()


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    # Переходим на страницу авторизации
    driver.get('https://start.rt.ru/')
    time.sleep(5)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_negative_aut_email_upper_case(driver):
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Вводим email
    driver.find_element(By.ID, 'username').send_keys(Data.email)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(Data.InvalidPasswordUpperCase)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем что появилась ошибка в авторизации
    wdw(driver, 60).until(EC.presence_of_element_located((By.ID, '/form-error-message')))
    # Проверяем, что мы оказались на главной странице пользователя
    # assert driver.current_url == "https://start.rt.ru/?tab=main"


def test_negative_aut_number_telephone_upper_case(driver):
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Вводим номер телефона
    driver.find_element(By.ID, 'username').send_keys(Data.NumberTelethon)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(Data.InvalidPasswordUpperCase)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем что появилась ошибка в авторизации
    wdw(driver, 60).until(EC.presence_of_element_located((By.ID, '/form-error-message')))
    # Проверяем, что мы оказались на главной странице пользователя
    # assert driver.current_url == "https://start.rt.ru/?tab=main"


def test_negative_aut_login_upper_case(driver):
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Вводим логин
    driver.find_element(By.ID, 'username').send_keys(Data.login)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(Data.InvalidPasswordUpperCase)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем что появилась ошибка в авторизации
    wdw(driver, 60).until(EC.presence_of_element_located((By.ID, '/form-error-message')))
    # Проверяем, что мы оказались на главной странице пользователя
    # assert driver.current_url == "https://start.rt.ru/?tab=main"


def test_negative_aut_email_lower_case(driver):
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Вводим email
    driver.find_element(By.ID, 'username').send_keys(Data.email)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(Data.InvalidPasswordUpperCase)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем что появилась ошибка в авторизации
    wdw(driver, 60).until(EC.presence_of_element_located((By.ID, '/form-error-message')))
    # Проверяем, что мы оказались на главной странице пользователя
    # assert driver.current_url == "https://start.rt.ru/?tab=main"


def test_negative_aut_number_telephone_lower_case(driver):
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Вводим номер телефона
    driver.find_element(By.ID, 'username').send_keys(Data.NumberTelethon)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(Data.InvalidPasswordUpperCase)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем что появилась ошибка в авторизации
    wdw(driver, 60).until(EC.presence_of_element_located((By.ID, '/form-error-message')))
    # Проверяем, что мы оказались на главной странице пользователя
    #assert driver.current_url == "https://start.rt.ru/?tab=main"


def test_negative_aut_login_lower_case(driver):
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Вводим логин
    driver.find_element(By.ID, 'username').send_keys(Data.login)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(Data.InvalidPasswordLowerCase)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    # Проверяем что появилась ошибка в авторизации
    wdw(driver, 60).until(EC.presence_of_element_located((By.ID, '/form-error-message')))
    # Проверяем, что мы оказались на главной странице пользователя
    # assert driver.current_url == "https://start.rt.ru/?tab=main"