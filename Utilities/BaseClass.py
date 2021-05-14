import pytest
import logging
import inspect

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):

        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        file_handler = logging.FileHandler("..\\Report\\logfile.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger

    def valifylinkpresence(self, Text):

        wait = WebDriverWait(self.driver, 7)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, Text)))

    def select_option(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
