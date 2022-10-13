import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from decouple import config

driver = webdriver.Chrome()
driver.get(config('URL_SCRAPING'))
driver.maximize_window()
alert = Alert(driver)

formFields = ['name', 'country', 'city', 'card', 'month', 'year']


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
    time.sleep(1)


def save_data_from_txt():
    with open('form_data_order.txt', encoding='utf-8') as f:
        data = f.read().splitlines()
        return data


def place_order():
    data = save_data_from_txt()
    driver.find_element(By.XPATH, "//button[contains(text(),\'Place Order\')]").click()
    time.sleep(1)

    for field in formFields:
        driver.find_element(By.ID, field).send_keys(data[formFields.index(field)])
        time.sleep(1)

    driver.find_element(By.XPATH, "//button[contains(text(),\'Purchase\')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),\'OK\')]").click()
    time.sleep(2)


def logout():
    driver.find_element(By.ID, "logout2").click()
    time.sleep(1)


def exit_browser():
    driver.quit()


def main():
    login()
    register()
    buy_articles("Phones", "Samsung galaxy s6")
    buy_articles("Phones", "Nexus 6")
    buy_articles("Laptops", "Sony vaio i5")
    buy_articles("Laptops", "Sony vaio i7")
    buy_articles("Monitors", "Apple monitor 24")
    buy_articles("Monitors", "ASUS Full HD")
    time.sleep(2)
    show_cart()

    place_order()
    logout()
    exit_browser()
