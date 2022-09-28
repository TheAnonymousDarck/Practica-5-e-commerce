import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from decouple import config

driver = webdriver.Chrome()
driver.get(config('URL_SCRAPING'))
alert = Alert(driver)


def register():
    driver.find_element(By.ID, "signin2").click()
    time.sleep(3)
    driver.find_element(By.ID, "sign-username").send_keys(config('USERNAME'))
    driver.find_element(By.ID, "sign-password").send_keys(config('PASSWORD'))
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),\'Sign up\')]").click()
    time.sleep(3)
    alert.accept()


def login():
    driver.find_element(By.ID, "login2").click()
    time.sleep(3)
    driver.find_element(By.ID, "loginusername").send_keys(config('USERNAME'))
    driver.find_element(By.ID, "loginpassword").send_keys(config('PASSWORD'))
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),\'Log in\')]").click()
    time.sleep(2)


def buy_articles(type, product):
    driver.find_element(By.XPATH, "//a[contains(text(),\'" + type + "\')]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[contains(text(),\'" + product + "\')]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//a[contains(text(),\'Add to cart\')]").click()
    time.sleep(2)
    alert.accept()
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[contains(text(),\'Home \')]").click()


def show_cart():
    driver.find_element(By.XPATH, "//a[contains(text(),\'Cart\')]").click()


register()
login()
time.sleep(2)

show_cart()
