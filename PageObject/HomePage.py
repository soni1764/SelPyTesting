from selenium.webdriver.common.by import By
from PageObject.ShoppingPage import ShoppingPage


class HomePage:
    shop = (By.XPATH, "//a[text()='Shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    radio = (By.CSS_SELECTOR, "#inlineRadio1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        self.driver = driver

    def click_shoppingpage(self):
        self.driver.find_element(*HomePage.shop).click()
        shoppingage = ShoppingPage(self.driver)
        return shoppingage

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def select_typeemployeeorstudent(self):
        return self.driver.find_element(*HomePage.radio)

    def click_tosubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_alert(self):
        return self.driver.find_element(*HomePage.alert)

    def get_screenshot(self):
        self.driver.get_screenshot_as_file("..\\Report\\Login.png")
