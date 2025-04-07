from selenium.webdriver.common.by import By
from base.base import BaseClass

class CartPage(BaseClass):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def find_price(self, shoppingList):
        actualPriceList=[]
        for item in shoppingList:
            #locator = "//td[normalize-space()='"+item+"']//parent::td//following-sibling::td"
            locator = "//td[normalize-space()='" + item + "']//following::td"
            price = self.wait_till_clickable(By.XPATH, locator).text
            price = float(price.strip('$'))
            actualPriceList.append(price)
        return actualPriceList

    def find_subtotal(self):
        cart_items = self.driver.find_elements(By.XPATH, "//tbody//tr")
        actual_subtotal={}
        for i in range(1, len(cart_items)+1):
            item = self.wait_until_element_present(By.XPATH, "//tbody//tr["+str(i)+"]//td[1]").text
            price = self.wait_until_element_present(By.XPATH, "//tbody//tr["+str(i)+"]//td[2]").text
            quantity = self.wait_until_element_present(By.XPATH, "//tr["+str(i)+"]//td[3]//input").get_attribute("value")
            subtotal = self.wait_until_element_present(By.XPATH, "//tbody//tr["+str(i)+"]//td[4]").text
            item_dict = { "name": item, "price": price, "quantity": quantity, "subtotal": subtotal}
            actual_subtotal.update({item : item_dict})
        return actual_subtotal