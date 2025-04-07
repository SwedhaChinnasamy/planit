import pytest
import softest
import logging
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class Test_Case1(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.ut = Utils(self.driver)
        logging.basicConfig(level=logging.DEBUG, filename="test1_debug.log", filemode="w")
        #logging.basicConfig(filename="test1_summary.log", filemode="w")

    def test_case_1(self):

        # Step 1: Launch the web application and go from home page go to Contact Page
        logging.info("Move to Contact Page")
        cp = self.hp.go_to_contact_page()

        # Step 2: Submit feedback without filling any mandatory fields
        logging.info("Submit without filling mandatory fields")
        cp.submit_message(submit=True)

        # Step 3: Verify proper error messages are thrown
        logging.info("Validating if all the error messages are displayed")
        self.ut.validate_errors(By.CSS_SELECTOR, ("#forename-err", "#email-err", "#message-err"))

        # Step 4: Fill all the necessary fields without submitting
        logging.info("Filling all the mandatory fields")
        cp.submit_message(forename="Swedha", email="swedhac96@gmail.com", message="This is a test")

        # Step 5: Verify the errors have disappeared
        logging.info("Validating if all the error messages are disappeared")
        self.ut.validate_errors(By.CSS_SELECTOR, ("#forename-err", "#email-err", "#message-err"), False)
