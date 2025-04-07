import re
import softest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class gUtils(softest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def wait_until_element_present(self, type, locator):
        wait = WebDriverWait(self.driver, 30)
        return wait.until(EC.presence_of_element_located((type, locator)))

    def validate_errors(self, type, error_locator_list, found=True):
        for locator in error_locator_list:
            try:
                self.driver.find_element(type, locator).is_displayed()
                self.soft_assert(self.assertTrue,found)
                #assert found, "Error message displayed even after filling mandatory fields"
            except NoSuchElementException:
                self.soft_assert(self.assertFalse, found)
                #assert not found, "Error message not displayed"
            self.assert_all()

    def validate_success(self):
        found = True
        try:
            self.wait_until_element_present(By.XPATH, "//div[@class='alert alert-success']")
            self.driver.find_element(By.XPATH, "//a[normalize-space()='« Back']").click()
        except NoSuchElementException:
            found = False
        self.soft_assert(self.assertTrue, found, msg=f"Feedback was not submitted")

    def validate_price(self, shopping_list, expected_price_list, actual_price_list):
        for i in range(0, len(actual_price_list)):
            #print(f"Item: {shopping_list[i]}, Expected_Price: {expected_price_list[i]}, Actual Price: {actual_price_list[i]}")
            self.soft_assert(self.assertEqual, expected_price_list[i], actual_price_list[i],
                             msg=f"The price for {shopping_list[i]} does not match the actual price.")

    def strip_and_convert_to_float(self, str):
        return(float(re.sub("[^0-9.]", "", str)))

    def find_strip_convert_to_float(self, type, locator):
        elem = self.driver.find_element(type, locator)
        float_value = self.strip_and_convert_to_float(elem.text)
        return float_value

    '''def validate_subtotal1(self):
        cart_items = self.driver.find_elements(By.XPATH, "//tbody//tr")
        for i in range(1, len(cart_items)+1):
            item = self.driver.find_element(By.XPATH, "//tbody//tr["+str(i)+"]//td[1]").text
            price = self.find_strip_convert_to_float(By.XPATH, "//tbody//tr["+str(i)+"]//td[2]")
            quantity = int(self.driver.find_element(By.XPATH, "//tr["+str(i)+"]//td[3]//input").get_attribute("value"))
            subtotal = self.find_strip_convert_to_float(By.XPATH, "//tbody//tr["+str(i)+"]//td[4]")
            expected_subtotal = price * quantity
            print(f"Item: {item}, Price: {price}, Quantity: {quantity}, Expected Subtotal: {expected_subtotal}, Actual Subtotal: {subtotal}")
            self.soft_assert(self.assertEqual, expected_subtotal, subtotal,
                             msg=f"The subtotal for {item} is not correct.")
        #assert subtotal==price*quantity, f"The subtotal for the {item} is not correct"'''

    def validate_subtotal(self, item, details):
        name = details["name"]
        price = self.strip_and_convert_to_float(details["price"])
        quantity = int(details["quantity"])
        subtotal = self.strip_and_convert_to_float(details["subtotal"])
        expected_subtotal = price * quantity
        print(
            f"Item: {name}, Price: {price}, Quantity: {quantity}, Expected Subtotal: {expected_subtotal}, Actual Subtotal: {subtotal}")
        self.soft_assert(self.assertEqual, expected_subtotal, subtotal,
                         msg=f"The subtotal for {name} is not correct.")

    def validate_total(self):
        actual_total = self.find_strip_convert_to_float(By.XPATH, "//strong[@class='total ng-binding']")
        subtotal_elems = self.driver.find_elements(By.XPATH, "//td[4]")
        expected_total = 0
        for elem in subtotal_elems:
            expected_total += self.strip_and_convert_to_float(elem.text)

        print(f"Expected Total: {expected_total}, Actual Total: {actual_total}")
        self.soft_assert(self.assertEqual, expected_total, actual_total,
                         msg=f"The total does not match the sum of subtotal of all the items.")
        self.assert_all()
        #assert actual_total==expected_total, f"The total does not match the sum of subtotal of all the items"