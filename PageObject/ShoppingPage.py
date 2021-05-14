from selenium.webdriver.common.by import By
from PageObject.CheckoutPage import CheckoutPage


class ShoppingPage:

    title = (By.CSS_SELECTOR, ".card-title")
    item_selected = (By.CSS_SELECTOR, ".btn-info")
    nextpage = (By.CSS_SELECTOR, ".btn-primary")

    def __init__(self, driver):
        self.driver = driver

    def getcardtitle(self):
        return self.driver.find_elements(*ShoppingPage.title)

    def add_itemincard(self):
        return self.driver.find_element(*ShoppingPage.item_selected)

    def click_checkoutpage(self):
        self.driver.find_element(*ShoppingPage.nextpage).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage
