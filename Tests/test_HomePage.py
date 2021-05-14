from Utilities.BaseClass import BaseClass
from PageObject.HomePage import HomePage
from TestData.HomePageData import HomePageData

import pytest


class TestHomePage(BaseClass):

    def test_formsubmission(self, getdata):

        homepage = HomePage(self.driver)
        log = self.getlogger()

        # homepage.get_name().send_keys("Gourav")
        homepage.get_name().send_keys(getdata["Name"])
        log.info("Name is : " + getdata["Name"])

        # homepage.get_email().send_keys("xyz.gmail.com")
        homepage.get_email().send_keys(getdata["Email"])
        log.info("Email is : " + getdata["Email"])

        # homepage.get_password().send_keys("Password")
        homepage.get_password().send_keys(getdata["Password"])
        log.info("Password is : " + getdata["Password"])

        self.select_option(homepage.get_gender(), getdata["Gender"])
        log.info("Gender is : " + getdata["Gender"])

        homepage.select_typeemployeeorstudent().click()
        homepage.click_tosubmit().click()

        alertext = homepage.get_alert().text
        log.info(alertext)
        assert "Success" in alertext
        homepage.get_screenshot()
        self.driver.refresh()

    # @pytest.fixture(params=[("Gourav", "xyz@gmail.com", "pass1", "Male"),("Aman", "aman@xyz.com", "pass2", "Female")])
    # @pytest.fixture(params=HomePageData.test_home_page_data)
    @pytest.fixture(params=HomePageData.getTestdata("Testcase2"))
    def getdata(self, request):
        return request.param
