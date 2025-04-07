from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from base.base import BaseClass
from utilities.utils import Utils

class ContactPage(BaseClass):
    log = Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def submit_message(self, forename="", email="", message="", submit=False):
        if forename != "":
            forename_element = self.wait_till_clickable(By.ID, "forename")
            self.log.debug("Clearing forename text box")
            forename_element.clear()
            self.log.debug(f"Sending '{forename}' to forename textbox")
            forename_element.send_keys(forename)

        if email != "":
            email_element = self.wait_till_clickable(By.ID, "email")
            self.log.debug("Clearing email text box")
            email_element.clear()
            self.log.debug(f"Sending '{email}' to email text box")
            email_element.send_keys(email)

        if message != "":
            message_element = self.wait_till_clickable(By.ID, "message")
            self.log.debug("Clearing message text box")
            message_element.clear()
            self.log.debug(f"Sending '{message}' to message text box")
            message_element.send_keys(message)

        if submit:
            submit_element = self.wait_till_clickable(By.LINK_TEXT, "Submit")
            self.log.info("Submitting the feedback")
            submit_element.click()

    def go_back_to_contact(self):
        self.wait_till_clickable(By.LINK_TEXT, "« Back").send_keys(Keys.ENTER)
        for i in range(5):
            try:
                self.driver.find_element(By.LINK_TEXT, "« Back").send_keys(Keys.ENTER)
            except NoSuchElementException:
                break

