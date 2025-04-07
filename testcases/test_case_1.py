import pytest
import softest
import logging
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestCase1(softest.TestCase):
    log = Utils.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.ut = Utils(self.driver)

    def test_case_1(self):

        # Step 1: Launch the web application and go from home page go to Contact Page
        self.log.info("Test Case 1: Submitting Feedback without mandatory fields and verifying error messages\n")
        self.log.info("Step 1: Launching webpage and going to Contact Page")
        cp = self.hp.go_to_contact_page()

        # Step 2: Submit feedback without filling any mandatory fields
        self.log.info("Step 2: Submitting Feedback without mandatory fields")
        cp.submit_message(submit=True)

        # Step 3: Verify proper error messages are thrown
        self.log.info("Step 3: Verifying if expected error are reported")
        self.ut.validate_errors(By.CSS_SELECTOR, ("#forename-err", "#email-err", "#message-err"))

        # Step 4: Fill all the necessary fields without submitting
        self.log.info("Step 4: Filling all the mandatory fields")
        cp.submit_message(forename="Swedha", email="swedhac96@gmail.com", message="This is a test")

        # Step 5: Verify the errors have disappeared
        self.log.info("Step 5: Verifying that previously reported error are gone")
        self.ut.validate_errors(By.CSS_SELECTOR, ("#forename-err", "#email-err", "#message-err"), False)
        self.log.info("Test Case 1: Complete\n")
