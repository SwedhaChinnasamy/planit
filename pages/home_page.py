import time
from selenium.webdriver.common.by import By
from base.base import BaseClass
from pages.cart_page import CartPage
from pages.contact_page import ContactPage
from pages.shop_page import ShopPage


class HomePage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_contact_page(self):
        self.driver.find_element(By.LINK_TEXT, "Contact").click()
        cp = ContactPage(self.driver)
        return cp

    def go_to_shop_page(self):
        self.driver.find_element(By.LINK_TEXT, "Shop").click()
        sp = ShopPage(self.driver)
        return sp

    def go_to_cart(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Cart").click()
        cart = CartPage(self.driver)
        return cart
