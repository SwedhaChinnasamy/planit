from selenium.webdriver.common.by import By
from base.base import BaseClass

class CartPage(BaseClass):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def find_price(self, shopping_list):
        actual_price_list=[]
        for item in shopping_list:
            #locator = "//td[normalize-space()='"+item+"']//parent::td//following-sibling::td"
            locator = "//td[normalize-space()='" + item + "']//following::td"
            price = self.wait_till_clickable(By.XPATH, locator).text
            price = float(price.strip('$'))
            actual_price_list.append(price)
        return actual_price_list
