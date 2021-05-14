from selenium.webdriver.common.by import By
from PageObject.ConfirmPage import ConfirmPage


class CheckoutPage:

    cnf_btn = (By.CSS_SELECTOR, ".btn-success")

    def __init__(self, driver):
        self.driver = driver

    def finalcheckout(self):
        self.driver.find_element(*CheckoutPage.cnf_btn).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
