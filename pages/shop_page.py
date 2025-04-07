from selenium.webdriver.common.by import By
from base.base import BaseClass
from utilities.utils import Utils

class ShopPage(BaseClass):
    log = Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def add_to_cart(self, shopping_list, quantity_list):
        for item in shopping_list:
            locator = "//h4[text()='"+item+"']//parent::div//child::a"
            item_elem = self.wait_till_clickable(By.XPATH,locator)
            i = quantity_list[shopping_list.index(item)]

            while i > 0:
                self.log.info(f"Adding {item} to cart")
                item_elem.click()
                i -= 1

    def find_price(self, shopping_list):
        expected_price_list = []
        for item in shopping_list:
            locator = "//h4[text()='"+item+"']/parent::div//child::span"
            price = self.driver.find_element(By.XPATH, locator).text
            price = float(price.strip('$'))
            expected_price_list.append(price)
        return expected_price_list
