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
    driver.get('https://lk.rt.ru/')

    driver.maximize_window()
    yield driver

    driver.quit()


def test_aut_email(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Вводим email
    driver.find_element(By.ID, 'username').send_keys(Data.email)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(Data.password)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"root"]'
                                                                    '/div/div/div[2]/div/div/div[2]/div[3]')))
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.current_url == 'https://start.rt.ru/?tab=main'


def test_aut_number_telephone(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Вводим номер телефона
    driver.find_element(By.ID, 'username').send_keys(Data.NumberTelethon)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(Data.password)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"root"]'
                                                                    '/div/div/div[2]/div/div/div[2]/div[3]')))
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.current_url == 'https://start.rt.ru/?tab=main'


def test_aut_login(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Вводим логин
    driver.find_element(By.ID, 'username').send_keys(Data.login)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(Data.password)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    wdw(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"root"]'
                                                                    '/div/div/div[2]/div/div/div[2]/div[3]')))
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.current_url == 'https://start.rt.ru/?tab=main'