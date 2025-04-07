from selenium.webdriver.common.by import By
from base.base import BaseClass

class ShopPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def add_to_cart(self, shoppingList, quantityList):
        for item in shoppingList:
            locator = "//h4[text()='"+item+"']//parent::div//child::a"
            item_elem = self.wait_till_clickable(By.XPATH,locator)
            i = quantityList[shoppingList.index(item)]

            while i > 0:
                item_elem.click()
                i -= 1

    def find_price(self, shoppingList):
        expectedPriceList = []
        for item in shoppingList:
            locator = "//h4[text()='"+item+"']/parent::div//child::span"
            price = self.driver.find_element(By.XPATH, locator).text
            price = float(price.strip('$'))
            expectedPriceList.append(price)
        return expectedPriceList
