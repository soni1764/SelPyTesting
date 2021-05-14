from Utilities.BaseClass import BaseClass
from PageObject.HomePage import HomePage


class Test2(BaseClass):

    def test_e2e(self):

        log = self.getlogger()
        homepage = HomePage(self.driver)                   # Homepage

        shoppingpage = homepage.click_shoppingpage()       # Shopping page

        log.info("Getting all the cards title")
        cards = shoppingpage.getcardtitle()
        # print("No of cards on this page is : ", len(cards))
        for card in cards:
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                shoppingpage.add_itemincard().click()
                print("Selected card is ", cardText)

        checkoutpage = shoppingpage.click_checkoutpage()     # Checkout page

        confirmpage = checkoutpage.finalcheckout()           # Confirm page
        log.info("Entering Country name")
        confirmpage.enter_countryname().send_keys("ind")

        self.valifylinkpresence("India")
        confirmpage.select_country().click()
        confirmpage.click_checkbox().click()
        confirmpage.click_topurchage().click()

        alert_text = confirmpage.get_alert().text
        print(alert_text)
        log.info(alert_text)
        assert "Success" in alert_text

        confirmpage.get_screenshot()
