from selenium.webdriver.common.by import By
from base.base import BaseClass

class ContactPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def submit_message(self, forename="", email="", message="", submit=False):
        if forename != "":
            forename_element = self.wait_till_clickable(By.ID, "forename")
            forename_element.clear()
            forename_element.send_keys(forename)

        if email != "":
            email_element = self.wait_till_clickable(By.ID, "email")
            email_element.clear()
            email_element.send_keys(email)

        if message != "":
            message_element = self.wait_till_clickable(By.ID, "message")
            message_element.clear()
            message_element.send_keys(message)

        if submit:
            submit_element = self.wait_till_clickable(By.LINK_TEXT, "Submit")
            submit_element.click()
