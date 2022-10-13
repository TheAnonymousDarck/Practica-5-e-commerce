import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from decouple import config
import time
import functions


class TestECommerce(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        driver = cls.driver
        driver.get(config('URL_SCRAPING'))
        driver.maximize_window()
        driver.implicitly_wait(5)
        cls.alert = Alert(cls.driver)
        cls.data = functions.save_data_from_txt()
        cls.formFields = ['name', 'country', 'city', 'card', 'month', 'year']
        cls.articles = {
            'Phones': 'Samsung galaxy s6',
            'Phones': 'Nexus 6',
            'Laptops': 'Sony vaio i5',
            'Laptops': 'Sony vaio i7',
            'Monitors': 'Apple monitor 24',
        }

    def test_0_register(self):
        driver = self.driver
        driver.find_element(By.ID, "signin2").click()
        time.sleep(3)
        driver.find_element(By.ID, "sign-username").send_keys(config('USERNAME'))
        driver.find_element(By.ID, "sign-password").send_keys(config('PASSWORD'))
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),\'Sign up\')]").click()
        time.sleep(3)
        self.alert.accept()

    def test_1_login(self):
        print('si entro al login')
        driver = self.driver
        driver.find_element(By.ID, "login2").click()
        time.sleep(3)
        driver.find_element(By.ID, "loginusername").send_keys(config('USERNAME'))
        driver.find_element(By.ID, "loginpassword").send_keys(config('PASSWORD'))
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),\'Log in\')]").click()
        time.sleep(2)

    def test_2_buy_articles(self):
        driver = self.driver
        for type, product in self.articles.items():
            driver.find_element(By.XPATH, "//a[contains(text(),\'" + type + "\')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//a[contains(text(),\'" + product + "\')]").click()
            time.sleep(3)
            driver.find_element(By.XPATH, "//a[contains(text(),\'Add to cart\')]").click()
            time.sleep(2)
            self.alert.accept()
            time.sleep(2)
            driver.find_element(By.XPATH, "//a[contains(text(),\'Home \')]").click()

        print('paso la compra')

    def test_3_show_cart(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//a[contains(text(),\'Cart\')]").click()
        time.sleep(1)
        print('si entro al carrito')

    def test_4_fill_form(self):
        driver = self.driver
        print('vas a dar click al boton')
        driver.find_element(By.XPATH, "//button[contains(text(),\'Place Order\')]").click()
        time.sleep(1)
        print('vas a dar click al boton')
        print('si entro al formulario')

        for field in self.formFields:
            driver.find_element(By.ID, field).send_keys(self.data[self.formFields.index(field)])
            time.sleep(1)

        driver.find_element(By.XPATH, "//button[contains(text(),\'Purchase\')]").click()
        print('si entro al purchase')
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),\'OK\')]").click()
        print('da ok')
        time.sleep(2)

    def test_5_logout(self):
        self.driver.find_element(By.ID, "logout2").click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HtmlTestRunner.HTMLTestRunner(output='reportes', report_name='test_ecommerce'))
