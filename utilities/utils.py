import inspect
import logging
import re
import softest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utils(softest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def wait_until_element_present(self, type, locator):
        wait = WebDriverWait(self.driver, 60)
        return wait.until(EC.presence_of_element_located((type, locator)))

    def wait_till_clickable(self, type, locator):
        wait = WebDriverWait(self.driver, 60)
        return wait.until(EC.element_to_be_clickable((type, locator)))

    def strip_and_convert_to_float(self, str):
        return float(re.sub("[^0-9.]", "", str))

    def find_strip_convert_to_float(self, type, locator):
        elem = self.driver.find_element(type, locator)
        return self.strip_and_convert_to_float(elem.text)

    def validate_errors(self, type, error_locator_list, found=True):
        for locator in error_locator_list:
            try:
                self.driver.find_element(type, locator).is_displayed()
                self.soft_assert(self.assertTrue,found)
            except NoSuchElementException:
                self.soft_assert(self.assertFalse, found)

    def validate_success(self):
        found = True
        try:
            self.wait_until_element_present(By.XPATH, "//div[@class='alert alert-success']")
        except NoSuchElementException:
            found = False
        self.soft_assert(self.assertTrue, found, msg=f"Feedback was not submitted")

    def validate_price(self, shopping_list, expected_price_list, actual_price_list):
        log = Utils.custom_logger()
        for i in range(0, len(actual_price_list)):
            log.debug(f"Verifying price of {shopping_list[i]}")
            self.soft_assert(self.assertEqual, expected_price_list[i], actual_price_list[i],
                             msg=f"The price for {shopping_list[i]} does not match the actual price.")

    def validate_subtotal(self):
        log = Utils.custom_logger()
        cart_items = self.driver.find_elements(By.XPATH, "//tbody//tr")
        for i in range(1, len(cart_items)+1):
            item = self.driver.find_element(By.XPATH, "//tbody//tr["+str(i)+"]//td[1]").text
            price = self.find_strip_convert_to_float(By.XPATH, "//tbody//tr["+str(i)+"]//td[2]")
            quantity = int(self.driver.find_element(By.XPATH, "//tr["+str(i)+"]//td[3]//input").get_attribute("value"))
            subtotal = self.find_strip_convert_to_float(By.XPATH, "//tbody//tr["+str(i)+"]//td[4]")
            expected_subtotal = price * quantity
            log.debug(f"Verifying subtotal of {item}")
            self.soft_assert(self.assertEqual, expected_subtotal, subtotal,
                             msg=f"The subtotal for {item} is not correct.")

    def validate_total(self):
        log = Utils.custom_logger()
        actual_total = self.find_strip_convert_to_float(By.XPATH, "//strong[@class='total ng-binding']")
        subtotal_elems = self.driver.find_elements(By.XPATH, "//td[4]")
        expected_total = 0
        for elem in subtotal_elems:
            expected_total += self.strip_and_convert_to_float(elem.text)

        log.debug("Verifying the total cost of the cart")
        self.soft_assert(self.assertEqual, expected_total, actual_total,
                         msg=f"The total does not match the sum of subtotal of all the items.")
        self.assert_all()

    @staticmethod
    def custom_logger(log_level=logging.DEBUG):
        #set logger name
        logger_name = inspect.stack()[1][3]

        #create logger and set log level
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)

        #create stream handler and file handler
        ch = logging.StreamHandler()
        fh = logging.FileHandler("logfile.log")

        #create formatter
        #formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        #add formatter to stream and file handler
        logger.addHandler(ch)
        logger.addHandler(fh)

        return logger