import pytest
import softest
from pages.home_page import HomePage
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestCase3(softest.TestCase):
    log = Utils.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.ut = Utils(self.driver)

    def test_case_3(self):
        shopping_list = ["Stuffed Frog", "Fluffy Bunny", "Valentine Bear"]
        quantity_list = [2, 5, 3]

        # Step 1: Go to Shop Page
        self.log.info("Test Case 3: Adding items to cart and verifying price, subtotal and total\n")
        self.log.info("Step 1: Launching webpage and going to Shop Page")
        sp = self.hp.go_to_shop_page()

        # Step 2: Buy 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear
        self.log.info("Step 2: Add items to cart")
        sp.add_to_cart(shopping_list, quantity_list)
        expected_price_list = sp.find_price(shopping_list)

        # Step 3: Go to the cart page
        self.log.info("Step 3: Go to cart")
        cart = self.hp.go_to_cart()
        actual_price_list = cart.find_price(shopping_list)

        # Step 4: Verify the price for each product
        self.log.info("Step 4: Verify the price of each product in cart")
        self.ut.validate_price(shopping_list, expected_price_list, actual_price_list)

        # Step 5: Verify the subtotal for each product is correct
        self.log.info("Step 5: Verify the subtotal of each item in cart")
        self.ut.validate_subtotal()

        # Step 6: Verify that total = sum(sub totals)
        self.log.info("Step 6: Verify the total of the cart")
        self.ut.validate_total()

        self.log.info("Test Case 3: Complete\n")
