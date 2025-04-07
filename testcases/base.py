import pytest
import softest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class Test_Cases(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.ut = Utils(self.driver)

    def test_case_1(self):

        # Step 1: Launch the web application and go from home page go to Contact Page
        cp = self.hp.go_to_contact_page()

        # Step 2: Submit feedback without filling any mandatory fields
        cp.submit_message(submit=True)

        # Step 3: Verify proper error messages are thrown
        self.ut.validate_errors(By.CSS_SELECTOR, ("#forename-err", "#email-err", "#message-err"))

        # Step 4: Fill all the necessary fields without submitting
        cp.submit_message(forename="Swedha", email="swedhac96@gmail.com", message="This is a test")

        # Step 5: Verify the errors have disappeared
        self.ut.validate_errors(By.CSS_SELECTOR, ("#forename-err", "#email-err", "#message-err"), False)

    @pytest.mark.parametrize('n', [1,2,3,4,5])
    def test_case_2(self, n):
        #Step 1: From the home page go to contact page
        print(f"Test Case 2: Run {n}")
        cp = self.hp.go_to_contact_page()

        #Step 2 & 3: Populate mandatory fields and click submit
        cp.submit_message(forename="John", email="John@example.com", message="This is a test", submit=True)

        #Step 4:Validate successful submission message
        self.ut.validate_success()

    def test_case_3(self):
        shopping_list = ["Stuffed Frog", "Fluffy Bunny", "Valentine Bear"]
        quantity_list = [2, 5, 3]

        # Step 1: Go to Shop Page
        sp = self.hp.go_to_shop_page()

        # Step 2: Buy 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear
        sp.add_to_cart(shopping_list, quantity_list)
        expected_price_list = sp.find_price(shopping_list)

        # Step 3: Go to the cart page
        cart = self.hp.go_to_cart()
        actual_price_list = cart.find_price(shopping_list)

        # Step 4: Verify the subtotal for each product is correct
        self.ut.validate_subtotal()

        # Step 5: Verify the price for each product
        self.ut.validate_price(shopping_list, expected_price_list, actual_price_list)

        # Step 6: Verify that total = sum(sub totals)
        self.ut.validate_total()
