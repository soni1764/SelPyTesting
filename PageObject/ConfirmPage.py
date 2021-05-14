from selenium.webdriver.common.by import By


class ConfirmPage:
    inputcountryname = (By.ID, "country")
    country = (By.LINK_TEXT, "India")
    checkbox = (By.CSS_SELECTOR, ".checkbox-primary")
    btn = (By.CSS_SELECTOR, ".btn-success")
    alert = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        self.driver = driver

    def enter_countryname(self):
        return self.driver.find_element(*ConfirmPage.inputcountryname)

    def select_country(self):
        return self.driver.find_element(*ConfirmPage.country)

    def click_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def click_topurchage(self):
        return self.driver.find_element(*ConfirmPage.btn)

    def get_alert(self):
        return self.driver.find_element(*ConfirmPage.alert)

    def get_screenshot(self):
        self.driver.get_screenshot_as_file("..\\Report\\screen.png")
